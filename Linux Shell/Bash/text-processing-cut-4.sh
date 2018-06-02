#!/bin/bash

while IFS= read -r line
do
    echo $line | cut -c1-4
done
