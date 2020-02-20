<?php

/**
 * @see https://www.hackerrank.com/challenges/append-and-delete/problem
 */

function appendAndDelete($s, $t, $k) {

  if ($k > strlen($s) + strlen($t)) {
    return "Yes";
  }

 for ($i = 0; $i <= strlen($s); $i++) {
    if (!str_begins($s, $t, $i + 1)) {
      echo "Last matching substring found is '" . substr($s, 0, $i) . "' ";
      $operations = ((strlen($s)) - $i) + (strlen($t) - $i);
      if ($operations === $k) {
        return "Yes";
      }
      elseif ($operations > $k) {
        return "No";
      }  
      elseif (($operations - $k) % 2 === 0) {
        return "Yes";
      }

      return "No";
    }
  }

  return "Yes";
}

function str_begins($haystack, $needle, $length) {
  return 0 === substr_compare($haystack, $needle, 0, $length);
}

# Run tests when the '--run-tests' parameter 
# is passed when executing the script.
if (in_array('--run-tests', $argv)) {
  compareTestCase("Yes", appendAndDelete("hackerhappy", "hackerrank", 9));
  compareTestCase("No", appendAndDelete("ashley", "ash", 2));
  compareTestCase("Yes", appendAndDelete("aba", "aba", 7));
  compareTestCase("No", appendAndDelete("y", "yu", 2));
  compareTestCase("Yes", appendAndDelete("aaaaaaaaaa", "aaaaa", 7));
  compareTestCase("Yes", appendAndDelete("abcdef", "fedcba", 15));
  compareTestCase("Yes", appendAndDelete("zzzzz", "zzzzzzz", 4));
  compareTestCase("No", appendAndDelete("asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv", "bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv", 100));
}

function compareTestCase($expected, $actual, $input_args = []) {
  echo !empty($input_args) ? implode(', ', $input_args) . " | " : "";
  echo "{$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
