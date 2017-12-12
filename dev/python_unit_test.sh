#!/usr/bin/env bash

set -e

# unit test
echo "Python Unit Tests"
nosetests --logging-level=INFO -v