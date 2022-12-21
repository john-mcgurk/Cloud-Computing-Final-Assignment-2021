<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: application/json");
require('functions.inc.php');

//No need for error handling - Only values that can be passed in are postive integers.
//No instance where there is missing param values either
$output = array(
	"error" => false,
	"string" => "",
	"answer" => 0
);

$x = $_REQUEST['x'];
$y = $_REQUEST['y'];


//print is_int($y);

if (is_numeric($x) and is_numeric($y)) {
	$answer=add($x,$y);
	$output['string']=$x."+".$y."=".$answer;
	$output['answer']=$answer;
} else {
	$output['error']="true";
	$output['answer']="undefined";
	$output['string']="Error with params -  Not numerical values";
}


echo json_encode($output);
exit();
