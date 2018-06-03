#!/bin/bash

readarray -t arr

for i in "${!arr[@]}"
do
    arr[$i]=".${arr[$i]:1}"
done

echo ${arr[@]}
