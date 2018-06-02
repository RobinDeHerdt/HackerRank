#!/bin/bash

# 1. Print the occurrences of the current characters
# 2. Remove weird whitespace from previous command output
# 3. Delimit on space, select the second field
uniq -c -i | tr -s ' ' | cut -d ' ' -f 2-
