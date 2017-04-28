<?php


define('DBHOST', 'localhost'); 			 // mysql host
define('DBUSER', 'juwilie_scan'); 		 // mysql username
define('DBPASS', 'he$e5UduCRu6');		 // mysql password
define('DBNAME', 'juwilie_scan');		 // mysql database name

$mysqli = new mysqli(DBHOST, DBUSER, DBPASS, DBNAME);

if ($mysqli->connect_errno) {
echo "MySQL connection error";
exit;
}

$mysqli->set_charset("utf8");
?>