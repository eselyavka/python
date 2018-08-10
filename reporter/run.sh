#!/bin/bash
set -Ce

PYTHON="$(which python2.7)"
PIP="$(which pip2.7)"

if [[ -z "${PYTHON}" ]] || [[ -z "${PIP}" ]] ; then
    echo "Need Python/Pip 2.7 to run"
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

    ${PIP} install virtualenv && \
    rm -rf -- env && \
    virtualenv -p "${PYTHON}" --prompt='(app-infra)' env && \
    source env/bin/activate && \
    pip2.7 install -r 'requirements.txt' && \
    python2.7 test_status_reporter.py && \
    python2.7 reporter.py ${input} ${output} && \
    deactivate && \
    rm -rf -- env

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
