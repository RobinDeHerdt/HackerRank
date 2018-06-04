#!/bin/bash

read n
readarray -t arr

echo "${arr[@]}" | tr ' ' '\n' | sort | uniq -u
