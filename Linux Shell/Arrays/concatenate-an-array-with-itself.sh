#!/bin/bash

# Read in the array, line per line
readarray -t arr

arr+=( "${arr[@]}" "${arr[@]}" )

echo ${arr[@]}
