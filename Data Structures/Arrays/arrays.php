<?php

/**
 * @see https://www.hackerrank.com/challenges/arrays-ds/problem
 */

function reverseArray($a) {
  return array_reverse($a);
}

# Run array manipulation tests when the '--run-tests' 
# parameter is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase("2 3 4 1", implode(' ', reverseArray([1, 4, 3, 2])));
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
