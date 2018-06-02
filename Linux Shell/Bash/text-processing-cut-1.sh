#!/bin/bash

while IFS= read -r line
do
    # This should work, but for some reason
    # it keeps failing at one specific test case.
    # echo ${line:2:1}

    # This however, does work for all test cases.
    echo $line | cut -c 3
done
