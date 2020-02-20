<?php

/**
 * @see https://www.hackerrank.com/challenges/picking-numbers/problem
 */

function pickingNumbers($a) {
  // List the amount of occurences for every value in the array.
  $value_count = array_count_values($a);

  // Sort the values based on key to make next value checking easier.
  ksort($value_count);

  $largest_count = 0;
  foreach ($value_count as $number => $count) {
    if (isset($value_count[$number+1])) {
      $total_count = $count + $value_count[$number+1];
    } else {
      // Special case: sometimes the amount of occurences of the number itself
      // is higher than the amount of occurences of other combinations.
      $total_count = $count;
    }
    }

    if ($total_count > $largest_count) {
      $largest_count = $total_count;
    }
  }

  return $largest_count;
}

# Run tests when the '--run-tests' parameter 
# is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase(5, pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5]));
  compareTestCase(3, pickingNumbers([4, 6, 5, 3, 3, 1]));
  compareTestCase(5, pickingNumbers([1, 2, 2, 3, 1, 2]));
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
