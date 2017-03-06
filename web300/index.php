<!DOCTYPE html>
<html>
<head>
<title>web300</title>
</head>
<body>
<h1>web300 website</h1>
<?php
if (empty($_GET['filename']))
$filename = 'index2';
else $filename = $_GET['filename'];
if (strpos($filename, '/') !== FALSE) $filename = 'index2';
include($filename.'.php');
?>
<p style="margin-top: 3000px;font-size: 6px; color: #FAFAFA;">Гугл не пройдет! А тебе слабо?</p>
</body>
</html>

