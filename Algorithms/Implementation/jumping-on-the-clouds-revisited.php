<?php

/**
 * @see https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
 */

    // Cloud types: 
    // - 0 = Cumulus cloud (normal)
    // - 1 = Thundercloud ( -2 energy )
function jumpingOnClouds($c, $k) {
  
  $energy = 100;

  $index = 0;
  while(TRUE) {

    // Make a jump - it costs 1 energy.
    $index += $k;
    $energy -= 1;

    // When we reach the end of the cloud array, we need to determine
    // whether we need to keep going or not. The game ends on index 0.
    if (!isset($c[$index])) {
      $out_of_bounds_amount = $index - (count($c) - 1);
      $index = $out_of_bounds_amount - 1;
      if ($index === 0)  {

        // The first cloud might be a thundercloud.
        if ($c[$index] === 1) {
          $energy -= 2;
        }

        return $energy;
      }
    }

    // Determine energy loss when landing on a thunder cloud.
    if ($c[$index] === 1) {
      $energy -= 2;
    }
  }
}

# Run tests when the '--run-tests' parameter 
# is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase(92, jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2));
  compareTestCase(80, jumpingOnClouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3));
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
