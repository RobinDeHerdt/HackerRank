#!/bin/bash

read number_count

sequence=($(cat)) 

sum=0
for n in ${sequence[@]}
do
  (( sum += n ))
done

printf %.3f $(echo "$sum/$number_count" | bc -l)
