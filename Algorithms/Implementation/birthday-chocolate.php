<?php

/**
 * @see https://www.hackerrank.com/challenges/the-birthday-bar/problem
 */

function birthday($pieces, $day, $month) {

  $matches = 0;
  foreach ($pieces as $key => $value) {

    $sum = $value;
    for ($i = 1; $i < $month; $i++) {

      $next_index = $key + $i;
      if (!isset($pieces[$next_index])) {

        // We've reached the end of the chocolate bar.
        // No valid matches can be found from this point on.
        return $matches;
      }

      $sum += $pieces[$next_index];
    }

    if ($sum === $day) {
      $matches++;
    }
  }

  return $matches;
}

# Run birtday chocolate tests when the '--run-tests' 
# parameter is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase(birthday([1, 2, 1, 3, 2], 3, 2), 2);
  compareTestCase(birthday([1, 1, 1, 1, 1, 1], 3, 2), 0);
  compareTestCase(birthday([4], 4, 1), 1);
  compareTestCase(birthday([5, 2, 2, 1, 5, 3, 2], 9, 3), 2);
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
