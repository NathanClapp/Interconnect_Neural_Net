#!/bin/bash

#start read loop before write

pipe=/tmp/zzz_testpipe

#removes pipe on program exit
trap "rm -f $pipe" EXIT

while true
do
    if read line <$pipe; then
        if [[ "$line" == 'quit' ]]; then
            break
        fi
        echo $line
    fi
done

echo "Reader exiting"