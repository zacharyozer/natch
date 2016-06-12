#!/usr/bin/env bash

SCRIPT_PATH=`dirname "$0"`
pushd $SCRIPT_PATH/../ >> /dev/null
npm test
popd >> /dev/null
