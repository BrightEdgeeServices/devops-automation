"""Test interactive settings entry against an external fake GitHub CLI."""

import json
import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "github-actions-config.sh"


def _read_calls(trace: Path) -> list[dict]:
    """Read calls recorded by the fake external CLI."""
    return [json.loads(line) for line in trace.read_text().splitlines()] if trace.exists() else []


def _run_session(transcript: str, directory: Path) -> subprocess.CompletedProcess:
    """Run the real Bash script with deterministic terminal input."""
    return subprocess.run(
        ["bash", str(SCRIPT)],
        capture_output=True,
        cwd=directory,
        input=transcript,
        text=True,
        timeout=10,
    )


class TestGithubActionsConfig:
    @pytest.mark.parametrize(
        ("choice", "target", "access", "kind", "destination"),
        [
            ("1", "RealTimeEvents", "2\n", "variable", ["--org", "RealTimeEvents", "--visibility", "private"]),
            ("2", "RealTimeEvents", "3\n", "secret", ["--org", "RealTimeEvents", "--visibility", "all"]),
            (
                "3",
                "RealTimeEvents/download_manager_app",
                "",
                "variable",
                ["--repo", "RealTimeEvents/download_manager_app"],
            ),
            (
                "4",
                "RealTimeEvents/download_manager_app",
                "",
                "secret",
                ["--repo", "RealTimeEvents/download_manager_app"],
            ),
        ],
    )
    def test_creates_each_setting_type(self, fake_github_cli, tmp_path, choice, target, access, kind, destination):
        value = "  example-$VALUE;$(false) with 'quotes' and \\slashes  "
        result = _run_session(f"{choice}\n{target}\n{access}sample_name\n{value}\nq\n", tmp_path)

        assert result.returncode == 0, result.stderr
        assert _read_calls(fake_github_cli) == [{"args": [kind, "set", "SAMPLE_NAME", *destination], "value": value}]
        assert value not in result.stdout + result.stderr

    def test_end_of_input_does_not_submit_a_partial_entry(self, fake_github_cli, tmp_path):
        result = _run_session("4\nRealTimeEvents/rteapi\nTOKEN\n", tmp_path)

        assert result.returncode == 0
        assert _read_calls(fake_github_cli) == []

    @pytest.mark.parametrize("status", [1, 2, 4])
    def test_failed_save_does_not_stop_following_entries(self, fake_github_cli, tmp_path, monkeypatch, status):
        monkeypatch.setenv("FAKE_GH_SAVE_STATUS", str(status))
        result = _run_session(
            "4\nRealTimeEvents/rteapi\nFAIL_ENTRY\nfirst-value\nGOOD_ENTRY\nsecond-value\nq\n", tmp_path
        )

        assert result.returncode == 0
        assert [call["args"][2] for call in _read_calls(fake_github_cli)] == ["FAIL_ENTRY", "GOOD_ENTRY"]
        assert "Saved FAIL_ENTRY" not in result.stdout
        assert "Saved GOOD_ENTRY" in result.stdout
        assert "first-value" not in result.stdout + result.stderr
        assert "second-value" not in result.stdout + result.stderr

    def test_literal_at_prefix_is_preserved(self, fake_github_cli, tmp_path):
        result = _run_session("3\nRealTimeEvents/rteapi\nVALUE\n@@literal\nq\n", tmp_path)

        assert result.returncode == 0
        assert _read_calls(fake_github_cli)[0]["value"] == "@literal"

    def test_missing_file_does_not_submit_a_setting(self, fake_github_cli, tmp_path):
        result = _run_session(f"4\nRealTimeEvents/rteapi\nTOKEN\n@{tmp_path / 'missing'}\nq\n", tmp_path)

        assert result.returncode == 0
        assert "Cannot read that input file" in result.stderr
        assert _read_calls(fake_github_cli) == []

    def test_multiline_file_is_sent_through_standard_input(self, fake_github_cli, tmp_path):
        value = "first test line\nsecond test line with $VALUE\n"
        source = tmp_path / "multiline-value.txt"
        source.write_text(value)
        result = _run_session(f"4\nRealTimeEvents/rteapi\nMULTILINE_VALUE\n@{source}\nq\n", tmp_path)

        assert result.returncode == 0
        call = _read_calls(fake_github_cli)[0]
        assert call["value"] == value
        assert call["args"] == ["secret", "set", "MULTILINE_VALUE", "--repo", "RealTimeEvents/rteapi"]
        assert value not in result.stdout + result.stderr

    def test_rejects_invalid_targets_and_names(self, fake_github_cli, tmp_path):
        result = _run_session(
            "3\nmissing-owner\nRealTimeEvents/rteapi\nBAD-NAME\nGITHUB_RESERVED\n1INVALID\nVALID_NAME\nvalue\nq\n",
            tmp_path,
        )

        assert result.returncode == 0
        assert "Invalid destination" in result.stdout
        assert [call["args"][2] for call in _read_calls(fake_github_cli)] == ["VALID_NAME"]

    def test_requires_authentication_before_any_settings(self, fake_github_cli, tmp_path, monkeypatch):
        monkeypatch.setenv("FAKE_GH_AUTH_FAILURE", "1")
        result = _run_session("q\n", tmp_path)

        assert result.returncode == 1
        assert "gh auth login" in result.stderr
        assert _read_calls(fake_github_cli) == []

    def test_selected_repository_access_is_explicit(self, fake_github_cli, tmp_path):
        result = _run_session("1\nRealTimeEvents\n1\ndownload_manager_app, rteapi\nVALUE\n42\nq\n", tmp_path)

        assert result.returncode == 0
        assert _read_calls(fake_github_cli)[0]["args"] == [
            "variable",
            "set",
            "VALUE",
            "--org",
            "RealTimeEvents",
            "--visibility",
            "selected",
            "--repos",
            "download_manager_app,rteapi",
        ]

    def test_switches_destinations_and_keeps_repeated_entry(self, fake_github_cli, tmp_path):
        result = _run_session(
            "1\nRealTimeEvents\n2\nFIRST\n1\nSECOND\nc\nc\n4\nBrightEdgeeServices/devops-automation\nLAST\nvalue\nq\n",
            tmp_path,
        )

        assert result.returncode == 0
        calls = _read_calls(fake_github_cli)
        assert [call["args"][0] for call in calls] == ["variable", "variable", "secret"]
        assert [call["args"][2] for call in calls] == ["FIRST", "SECOND", "LAST"]
        assert calls[1]["value"] == "c"
        assert calls[2]["args"][-2:] == ["--repo", "BrightEdgeeServices/devops-automation"]
