#!/usr/bin/env bash

GREEN='\033\x1B[0;34m'
NC='\033\x1B[0m' # No Color


SCRIPT_PATH=`dirname "$0"`
pushd $SCRIPT_PATH/../ >> /dev/null
PROJECT_ROOT=`pwd`
printf "${GREEN}Running JS tests${NC}\n"
npm test
popd >> /dev/null

export PYTHONPATH=$PROJECT_ROOT/src/python

printf "${GREEN}Running Python tests${NC}\n"
python $PROJECT_ROOT/test/python/natch_matcher_test.py
