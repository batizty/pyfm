#!/usr/bin/env bash

set -e


unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac
echo "OS is detected as: ${machine}"

# check code style
if [ $machine = "Linux" ]; then
    opt="-r"
else
    opt=""
fi

echo "check:..."

git diff master --name-only -- '*.py' \
    | xargs ${opt} flake8

echo "check: success."
