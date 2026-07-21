#!/bin/bash -i
#

# Safety check: must run from a directory named "tests"
# from a non-tests directory by mistake.
if [[ "$(basename "$PWD")" != "tests" ]]; then
    echo "ERROR: verify.sh must be run from a directory named 'tests'." >&2
    echo "  Current PWD: $PWD" >&2
    exit 1
fi

lpDo ../bin/bannaInfo.cs
lpDo ../bin/bannaInfo.cs -i bannaForEtcHosts
lpDo cp ./etcHosts.blank ./etcHosts
lpDo bannaInfo.cs -i updateEtcHosts  ./etcHosts

lpDo diff ./etcHosts.blank ./etcHosts

