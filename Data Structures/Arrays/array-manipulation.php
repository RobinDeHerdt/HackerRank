<?php

/**
 * @see https://www.hackerrank.com/challenges/crush/problem
 */

function arrayManipulationSimple($n, $queries) {
  $array = array_fill(1, $n, 0);
  foreach ($queries as $key => $query) {
    $index_start = $query[0];
    $index_end = $query[1];
    
    $k = $query[2];

    $sliced_array = array_slice($array, $index_start - 1, ($index_end - $index_start) + 1, TRUE);
    foreach ($sliced_array as $key => $value) {
      $sliced_array[$key] += $k;
    }

    $array = array_replace($array, $sliced_array);
  }

  return max($array);
}

function arrayManipulationComplex($n, $queries) {
  $array = [];
  foreach ($queries as $key => $query) {
    $index_start = $query[0];
    $index_end = $query[1] + 1;
    
    $value = $query[2];

    // Prevent warnings; initialize the
    // array key if it doesn't exist yet.
    if (!isset($array[$index_start])) {
      $array[$index_start] = 0;
    }

    // Prevent warnings; initialize the
    // array key if it doesn't exist yet.
    if (!isset($array[$index_end])) {
      $array[$index_end] = 0;
    }

    $array[$index_start] += $value;
    $array[$index_end] -= $value;
  }

  ksort($array);

  $max = 0;
  $sum = 0;
  foreach ($array as $key => $value) {
    $sum += $value;
    if ($sum > $max) {
      $max = $sum;
    }
  }

  return $max;
}

# Run array manipulation tests when the '--run-tests' 
# parameter is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase(arrayManipulationSimple(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]), 200);
  compareTestCase(arrayManipulationSimple(10, [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]), 31);

  compareTestCase(arrayManipulationComplex(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]), 200);
  compareTestCase(arrayManipulationComplex(10, [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]), 31);
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
