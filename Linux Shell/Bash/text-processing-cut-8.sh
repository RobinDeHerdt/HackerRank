#!/bin/bash

while IFS= read -r line
do
    echo $line | cut -d' ' -f1-3
done
