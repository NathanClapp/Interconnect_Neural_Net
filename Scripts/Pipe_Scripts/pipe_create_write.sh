#!/bin/bash

#start read loop before write

pipe=/tmp/zzz_testpipe

if [[ ! -p $pipe ]]; then
    mkfifo $pipe
fi

if [[ "$1" ]]; then
    echo "$1" >$pipe
else
    echo "Hello from $$" >$pipe
fi
