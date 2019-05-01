<!DOCTYPE html>
<html>
<head>
	<title>Data lul xdxd</title>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="description" content="">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta property="og:title" content="">
	<meta property="og:description" content="">
	<meta property="og:image" content="">
	<meta property="og:url" content="">
	<link rel="stylesheet" href="">
</head>
<body>

</body>
</html>

<?php

$file = file_read_contents("./data-gathering/posts/good-batch-2019.json");
$read = read_json($file);
echo $read;

 ?>