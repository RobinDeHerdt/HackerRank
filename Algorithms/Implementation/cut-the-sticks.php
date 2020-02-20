<?php

/**
 * @see https://www.hackerrank.com/challenges/cut-the-sticks/problem
 */

function cutTheSticks($arr, $solution) {

	$solution[] = count($arr);

	sort($arr);

	if (!isset($arr[0])) {
		return $solution;
	}

	if ($arr[0] === $arr[count($arr) - 1]) {
		return $solution;
	}

	$shortest = $arr[0];
	unset($arr[0]);

	foreach ($arr as $key => $value) {
		if ($value === $shortest || ($value - $shortest) === 0) {
			unset($arr[$key]);
			continue;
		}

	 	$arr[$key] = $value - $shortest;
	}

	return cutTheSticks($arr, $solution);
}

# Run tests when the '--run-tests' parameter 
# is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase([3, 2, 1], cutTheSticks([1, 2, 3], []));
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  $expected = implode(',', $expected);
  $actual = !empty($actual) ? implode(',', $actual) : 'empty array';
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
