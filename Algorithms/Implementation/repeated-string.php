<?php

/**
 * @see https://www.hackerrank.com/challenges/repeated-string/problem
 */

function repeatedString($s, $n) {
	$repeats = floor($n / strlen($s));
	$rest = $n % strlen($s);
	$final_repeating_string = substr($s, 0, $rest);
	$solution = (substr_count($s, 'a') * $repeats) + substr_count($final_repeating_string, 'a');

	echo "\n";
	$fact = gmp_fact(30);
	echo gmp_strval($fact);
	echo "\n";
	
	return (int) $solution;
}

# Run tests when the '--run-tests' parameter 
# is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase(7, repeatedString('aba', 10));
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
