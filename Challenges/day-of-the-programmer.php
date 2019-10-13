<?php

/**
 * @see https://www.hackerrank.com/challenges/day-of-the-programmer/problem
 */

function dayOfProgrammer($year) {

  $month_map = [
    "01" => 31,
    "02" => getAmountOfDaysInFebruary($year),
    "03" => 31,
    "04" => 30,
    "05" => 31,
    "06" => 30,
    "07" => 31,
    "08" => 31,
    "09" => 30,
    "10" => 31,
    "11" => 30,
    "12" => 31,
  ];

  $count = 0;
  foreach ($month_map as $month_number => $month_days) {
    if (($count + $month_days) > 256) {
      $day_number = 256 - $count;
      return "{$day_number}.{$month_number}.{$year}";
    }

    $count += $month_days;
  }
}

function getAmountOfDaysInFebruary($year) {
  if ($year >= 1700 && $year <= 1917) {
    return isJulianLeapYear($year) ? 29 : 28;

  } elseif ($year === 1918) {
    return 15;

  } elseif ($year >= 1919 && $year <= 2700) {
    return isGregorianLeapYear($year) ? 29 : 28;

  } else {
    throw new Exception("Year out of bounds");    
  }
}

function isJulianLeapYear($year) {
  if  ($year % 4 === 0) {
    return TRUE;
  }

  return FALSE;
}

function isGregorianLeapYear($year) {
  if ($year % 400 === 0) {
    return TRUE;
  }

  if ($year % 4 === 0 && $year % 100 !== 0) {
    return TRUE;
  }

  return FALSE;
}

# Calculate the day of the programmer using all numeric 
# parameters that are passed when executing the script.
foreach ($argv as $key => $value) {
  if (is_numeric($value)) {
    echo (int) $value . ": " . dayOfProgrammer((int) $value) . "\n";
  }
}

# Print every day of the programmer when the '--print-all' 
# parameter is passed when executing the script.
if (in_array('--print-all', $argv)) {
  for ($i = 1700; $i <= 2700; $i++) { 
    echo dayOfProgrammer($i) . "\n";
  }
}

# Run day of the programmer tests when the '--run-tests' 
# parameter is passed when executing the script.
if (in_array('--run-tests', $argv)) {

  # Julian calendar testcase
  compareTestCase(dayOfProgrammer(1800), "12.09.1800", [1800]);

  # Transition period testcase
  compareTestCase(dayOfProgrammer(1918), "26.09.1918", [1918]);

  # Gregorian calendar testcases
  compareTestCase(dayOfProgrammer(2016), "12.09.2016", [2016]);
  compareTestCase(dayOfProgrammer(2017), "13.09.2017", [2017]);
  compareTestCase(dayOfProgrammer(2018), "13.09.2018", [2018]);
}

function compareTestCase($expected, $actual, $input_args = []) {
  $parameter_info = !empty($input_args) ? implode(', ', $input_args) : "";
  echo "{$parameter_info} | {$expected} = {$actual}";
  echo $expected === $actual ? " \033[32m[PASS]\033[0m \n" : " \033[31m[FAIL]\033[0m \n";
}
