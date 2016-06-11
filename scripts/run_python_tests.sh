#!/usr/bin/env bash

SCRIPT_PATH=`dirname "$0"`
pushd $SCRIPT_PATH/../ >> /dev/null
PROJECT_ROOT=`pwd`
popd >> /dev/null

export PYTHONPATH=$PROJECT_ROOT/src/python

python $PROJECT_ROOT/test/python/natch_matcher_test.py
