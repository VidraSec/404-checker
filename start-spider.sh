#!/usr/bin/env bash

output_file="output.txt"

python3 start-spider.py | tee $output_file
output_len=($(wc -c $output_file)[0])

if [ $output_len -gt 0 ]
then
    echo "At least one HTTP error code detected."
    exit 1
fi
exit 0