<?php

/**
 * @see https://www.hackerrank.com/challenges/find-digits/problem
 */

function findDigits($n) {
  $result = 0;
  $string_n = (string) $n;
  foreach (str_split($string_n, 1) as $index => $digit) {
    $digit = (int) $digit;

    // Avoid dividing by 0.
    if ($digit === 0) {
      continue;
    }

    if ($n % $digit === 0) {
      $result++;
    }
  }

  return $result;
}

# Run tests when the '--run-tests' parameter 
# is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase(2, findDigits(12));
  compareTestCase(3, findDigits(1012));
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
