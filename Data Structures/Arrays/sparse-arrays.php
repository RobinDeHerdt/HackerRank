<?php

/**
 * @see https://www.hackerrank.com/challenges/arrays-ds/problem
 */

function matchingStrings($strings, $queries) {
	foreach ($queries as $key => $value) {
		$results[] = countAppearances($value, $strings);
	}

	return $results;
}

function countAppearances($string, $array) {
	$count = 0;
	foreach ($array as $key => $value) {
		if ($value === $string) {
			$count++;
		}
	}

	return $count;
}

# Run tests when the '--run-tests' parameter
# is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase("1 0 1", implode(' ', matchingStrings(["def", "de", "fgh"], ["de", "lmn", "fgh"])));
  compareTestCase("2 1 0", implode(' ', matchingStrings(["aba", "baba", "aba", "xzxb"], ["aba", "xzxb", "ab"])));
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
