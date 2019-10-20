<?php

/**
 * @see https://www.hackerrank.com/challenges/2d-array/problem
 */

function hourglassSum($arr) {
	$sums = [];
	foreach ($arr as $row_key => $row) {
		foreach ($row as $index => $value) {

			// Top of the hourglass.
			if (!isset($arr[$row_key][$index + 2])) {
				continue;
			}		

			// Middle of the hourglass.
			if (!isset($arr[$row_key + 1])) {
				continue;
			}

			// Bottom of the hourglass.
			if (!isset($arr[$row_key + 2][$index + 2])) {
				continue;
			}

			$sum = 0;
			for ($i = 0; $i < 3; $i++) {
				$sum += $arr[$row_key][$index + $i];
				$sum += $arr[$row_key + 2][$index + $i];
			}			
			$sum += $arr[$row_key + 1][$index + 1];

			$sums[] = $sum;
		}
	}

	return max($sums);
}

# Run all tests when the '--run-tests' parameter 
# is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase(19, hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]), ['Testcase 1']);
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
