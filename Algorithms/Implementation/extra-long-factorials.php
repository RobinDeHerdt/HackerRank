<?php

/**
 * @see https://www.hackerrank.com/challenges/extra-long-factorials/problem
 */
function extraLongFactorials($n) {
    return gmp_strval(gmp_fact($n));
}

# Run tests when the '--run-tests' parameter 
# is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase("265252859812191058636308480000000", extraLongFactorials(30));
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
