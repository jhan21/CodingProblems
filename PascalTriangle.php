<?php

function factorial($n) {
  if ($n <= 1) {
    return 1;
  }
  else {
    return $n * factorial($n - 1);
  }
}

function pascals_triangle($n) {
  // Your code here
  $answer = array();
  for ($x = 0; $x < $n; $x++) {
  	for ($y = 0; $y <= $x; $y++) {
  		array_push($answer, (factorial($x)/(factorial($y) * factorial($x - $y))));
  	}
  }
  print_r($answer);
  return($answer);
}

echo(factorial(8));
pascals_triangle(1);
