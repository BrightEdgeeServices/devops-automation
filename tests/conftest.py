"""External GitHub CLI stand-in for local helper tests."""

import os
from pathlib import Path
from textwrap import dedent

import pytest


@pytest.fixture
def fake_github_cli(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Record fake CLI calls without accessing GitHub or real credentials."""
    binary_directory = tmp_path / "bin"
    binary_directory.mkdir()
    executable = binary_directory / "gh"
    executable.write_text(dedent("""\
            #!/usr/bin/env python3
            import json
            import os
            from pathlib import Path
            import sys

            args = sys.argv[1:]
            if args[:2] == ["auth", "status"]:
                sys.exit(int(os.environ.get("FAKE_GH_AUTH_FAILURE", "0")))
            if args[:2] not in [["secret", "set"], ["variable", "set"]]:
                sys.exit("Unexpected CLI command")
            with Path(os.environ["FAKE_GH_CALLS_PATH"]).open("a") as stream:
                stream.write(json.dumps({"args": args, "value": sys.stdin.read()}) + "\\n")
            if args[2] == "FAIL_ENTRY":
                print("Simulated GitHub permission error", file=sys.stderr)
                sys.exit(int(os.environ.get("FAKE_GH_SAVE_STATUS", "1")))
            """))
    executable.chmod(0o755)
    trace = tmp_path / "calls.jsonl"
    monkeypatch.setenv("FAKE_GH_CALLS_PATH", str(trace))
    monkeypatch.setenv("PATH", f"{binary_directory}{os.pathsep}{os.environ['PATH']}")
    return trace
