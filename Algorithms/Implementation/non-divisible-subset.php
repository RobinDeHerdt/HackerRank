<?php

/**
 * @see https://www.hackerrank.com/challenges/non-divisible-subset/problem
 */
function nonDivisibleSubset($k, $s) {

	if  ($k === 1 || $k === 0) {
		return 1;
	}

	$remainders = [];
	foreach ($s as $key => $value) {
		$remainders[$key] = $value % $k;
	}

	$solutions = [];
	$count = 0;

	// Key = remainder
	// Value = remainder count
	$value_count = array_count_values($remainders);
	$replicated = $value_count;
	foreach ($value_count as $a => $a_count) {
	 	foreach ($value_count as $b => $b_count) {
	 		if ($a === $b || $b < $a) {
	 			continue;
	 		}

	 		if ($a + $b === $k) {
				if ($value_count[$a] >= $value_count[$b]) {
					$count += $value_count[$a];
				} else {
					$count += $value_count[$b];				
				}

				unset($replicated[$a]);
				unset($replicated[$b]);
			}
	 	}
	}

	foreach ($replicated as $a => $a_count) {
		if ($a === 0) {
			$count += 1;
			continue;
		}

		if ($k / $a === $a_count) {
			$count += $a_count;
			continue;
		}

		$count += $a_count;
	}

	return $count;
}

# Run tests when the '--run-tests' parameter 
# is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase(3, nonDivisibleSubset(3, [1, 7, 2, 4]));
  compareTestCase(11, nonDivisibleSubset(7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]));
  compareTestCase(1, nonDivisibleSubset(1, [1, 2, 3, 4, 5]));
  compareTestCase(5, nonDivisibleSubset(4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));
  compareTestCase(5, nonDivisibleSubset(9, [422346306, 940894801, 696810740, 862741861, 85835055, 313720373]));
  
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
