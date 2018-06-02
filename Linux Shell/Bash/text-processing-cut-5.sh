#!/bin/bash

while IFS= read -r line
do
    # Default cut delimiter is the TAB character.
    echo $line | cut -f-3
done
