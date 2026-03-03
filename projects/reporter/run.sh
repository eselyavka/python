#!/bin/bash
set -Ce

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
PYTHON="${PYTHON:-python3}"

if ! command -v "${PYTHON}" >/dev/null 2>&1 ; then
    echo "Need an available Python 3 interpreter"
    exit 2
fi

function test_runner() {
    local input=''
    local output=''

    if [[ -n "${1}" ]] ; then
        input="--input ${1}"
    fi

    if [[ -n "${2}" ]] ; then
        output="--output ${2}"
    fi

    cd "${REPO_ROOT}" && \
    "${PYTHON}" -m pip install -r 'projects/reporter/requirements.txt' && \
    "${PYTHON}" -m unittest projects.reporter.test_status_reporter -v && \
    "${PYTHON}" -m projects.reporter.reporter ${input} ${output}

    return $?
}

function usage() {
    echo -ne "${0} <input> <output>\n\n"
    exit 0
}

function parse_args() {
    while [[ $# -gt 0 ]] ; do
      case $1 in
        --help)
            usage
            ;;
        -h)
            usage
            ;;
      esac
      shift
    done
}

function main() {
    parse_args "$@"
    test_runner "${1}" "${2}"
}

main "${1}" "${2}"
