<?php

/**
 * @see https://www.hackerrank.com/challenges/library-fine/problem
 */


/**
 * 1: Return date
 * 2: Due return date
 */
function libraryFine($d1, $m1, $y1, $d2, $m2, $y2) {

	$returned =	DateTime::createFromFormat("d m Y", "$d1 $m1 $y1");
	$due =	DateTime::createFromFormat("d m Y", "$d2 $m2 $y2");
	if ($returned->getTimestamp() <= $due->getTimestamp()) {
		return 0;
	}

	if ($y1 === $y2 && $m1 === $m2) {
		$days_late = $d1 - $d2;
		return 15 * $days_late;
	}

	if ($y1 === $y2) {
		$months_late = $m1 - $m2;
		return 500 * $months_late;
	}

	return 10000;
}

# Run tests when the '--run-tests' parameter 
# is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase(45, libraryFine(9, 6, 2015, 6, 6, 2015));
  compareTestCase(10000, libraryFine(1, 1, 2016, 31, 12, 2015));
  compareTestCase(1500, libraryFine(5, 5, 2014, 23, 2, 2014));
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
