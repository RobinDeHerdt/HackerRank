<?php

/**
 * @see https://www.hackerrank.com/challenges/sherlock-and-squares/problem
 */


function squares($a, $b) {
  return (int) (floor(sqrt($b)) - ceil(sqrt($a))) + 1;
}

# Run tests when the '--run-tests' parameter 
# is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase(2, squares(3, 9));
  compareTestCase(0, squares(17, 24));
  compareTestCase(5, squares(9, 49));
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
