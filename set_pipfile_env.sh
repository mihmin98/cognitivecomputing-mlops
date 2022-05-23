#!/bin/bash

args=("$@")

if [[ ${args[0]} = "ml" ]]; then
    cp -f Pipfile.ml Pipfile
    cp -f Pipfile.lock.ml Pipfile.lock
elif [[ ${args[0]} = "app" ]]; then
    cp -f Pipfile.app Pipfile
    cp -f Pipfile.lock.app Pipfile.lock
else
    echo "bad args"
    exit 22
fi
