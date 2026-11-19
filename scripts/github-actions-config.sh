#!/usr/bin/env bash
# Interactive GitHub Actions configuration. Requires Bash and GitHub CLI (gh).
set +x
set -euo pipefail

github_destination_args=()
github_scope=""
github_setting_kind=""
github_target=""

choose_destination() {
  local choice visibility repositories

  while true; do
    printf '\n1) Organization variables\n2) Organization secrets\n3) Repository variables\n4) Repository secrets\n'
    read -r -p 'Destination [1-4, q to quit]: ' choice || return 1
    case "${choice,,}" in
      1) github_scope=organization; github_setting_kind=variable ;;
      2) github_scope=organization; github_setting_kind=secret ;;
      3) github_scope=repository; github_setting_kind=variable ;;
      4) github_scope=repository; github_setting_kind=secret ;;
      q) return 1 ;;
      *) printf 'Choose 1, 2, 3, 4, or q.\n'; continue ;;
    esac
    break
  done

  if [[ "$github_scope" == repository ]]; then
    read_target 'Repository (OWNER/REPO)' '^[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_.-]+$' || return 1
    github_destination_args=(--repo "$github_target")
  else
    read_target 'Organization (for example RealTimeEvents)' '^[A-Za-z0-9][A-Za-z0-9-]*$' || return 1
    while true; do
      printf '\nRepository access:\n1) Selected repositories\n2) All private repositories\n3) All repositories\n'
      read -r -p 'Access [1-3, q to quit]: ' choice || return 1
      case "${choice,,}" in
        1) visibility=selected ;;
        2) visibility=private ;;
        3) visibility=all ;;
        q) return 1 ;;
        *) printf 'Choose 1, 2, 3, or q.\n'; continue ;;
      esac
      break
    done
    github_destination_args=(--org "$github_target" --visibility "$visibility")
    if [[ "$visibility" == selected ]]; then
      while true; do
        read -r -p 'Repository names, comma-separated (q to quit): ' repositories || return 1
        [[ "${repositories,,}" != q ]] || return 1
        repositories="${repositories//[[:space:]]/}"
        if [[ "$repositories" =~ ^[A-Za-z0-9_.-]+(,[A-Za-z0-9_.-]+)*$ ]]; then
          github_destination_args+=(--repos "$repositories")
          break
        fi
        printf 'Enter repository names such as download_manager_app,rteapi.\n'
      done
    fi
    printf 'Organization repository access: %s%s\n' "$visibility" "${repositories:+ ($repositories)}"
  fi
  printf '\nDestination: %s %s / %s\n' "$github_scope" "$github_target" "$github_setting_kind"
}

main() {
  local setting_name status

  if ! command -v gh >/dev/null 2>&1; then
    printf 'GitHub CLI is required. On Fedora: sudo dnf install gh\n' >&2
    return 1
  fi
  export GH_HOST=github.com GH_PROMPT_DISABLED=1
  if ! gh auth status --hostname github.com >/dev/null 2>&1; then
    printf 'Sign in first: gh auth login --hostname github.com\n' >&2
    return 1
  fi
  printf 'Create or update GitHub Actions variables and secrets. Existing names are updated.\n'
  printf 'At the name prompt: c changes destination; q quits.\n'
  printf 'Values: enter one line, @/path/to/file for multiline input, or @@ for a literal leading @.\n'
  choose_destination || return 0

  while true; do
    read -r -p 'Name [c to change destination, q to quit]: ' setting_name || return 0
    case "${setting_name,,}" in
      c) choose_destination || return 0; continue ;;
      q) return 0 ;;
    esac
    setting_name="${setting_name^^}"
    if [[ ! "$setting_name" =~ ^[A-Z_][A-Z0-9_]*$ || "$setting_name" == GITHUB_* ]]; then
      printf 'Use letters, digits, and underscores; do not start with a digit or GITHUB_.\n'
      continue
    fi
    if save_setting "$setting_name"; then
      printf 'Saved %s to %s %s (%s).\n' "$setting_name" "$github_scope" "$github_target" "$github_setting_kind"
    else
      status=$?
      [[ "$status" != 2 ]] || return 0
      printf 'Could not save %s. Check the error, then enter the name again to retry, or c to change destination.\n' "$setting_name" >&2
    fi
  done
}

read_target() {
  local label=$1 pattern=$2 candidate

  while true; do
    read -r -p "$label (q to quit): " candidate || return 1
    [[ "${candidate,,}" != q ]] || return 1
    if [[ "$candidate" =~ $pattern ]]; then
      github_target=$candidate
      return 0
    fi
    printf 'Invalid destination. Try again.\n'
  done
}

save_setting() {
  local setting_name=$1 input_value input_file
  local -a command_args=("$github_setting_kind" set "$setting_name" "${github_destination_args[@]}")

  if [[ "$github_setting_kind" == secret ]]; then
    if ! IFS= read -r -s -p 'Secret value (hidden; @file supported): ' input_value; then
      printf '\n'
      return 2
    fi
    printf '\n'
  else
    IFS= read -r -p 'Value (@file supported): ' input_value || return 2
  fi

  # Use standard input so values never become gh command-line arguments.
  case "$input_value" in
    @@*) printf '%s' "${input_value:1}" | gh "${command_args[@]}" || return 1 ;;
    @*)
      input_file=${input_value:1}
      if [[ ! -f "$input_file" || ! -r "$input_file" ]]; then
        printf 'Cannot read that input file.\n' >&2
        return 1
      fi
      gh "${command_args[@]}" < "$input_file" || return 1
      ;;
    *) printf '%s' "$input_value" | gh "${command_args[@]}" || return 1 ;;
  esac
}

trap 'printf "\n"; exit 130' INT
main "$@"
