<?php
echo "Test Script Starting\n";
require('functions.inc.php');

$x=10;
$y=5;
$expect=15;

$answer=add($x,$y);

echo "Test Result: ".$x."+".$y."=".$answer." (expected: ".$expect.")\n";

if ($answer==$expect)
{
    echo "Test Passed\n";
    exit(0);
}
else
{
    echo "Test Failed\n";
    exit(1);
}
