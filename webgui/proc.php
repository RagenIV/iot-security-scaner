<?php
/**
 * Created by PhpStorm.
 * User: juwilie
 * Date: 4/29/17
 * Time: 12:16 AM
 */

include "db.php";

$advanced = 0;

if(isset($_POST['hostname']) && isset($_POST['email']))
{
    if(isset($_POST['adv']))
        $advanced = 1;
    $hostname = $mysqli->real_escape_string($_POST['hostname']);
    $email = $mysqli->real_escape_string($_POST['email']);
    $query = "INSERT INTO `requests`(`email`,`hostname`,`adv`) VALUES ('".$email."','".$hostname."','".$advanced."')";

    if($res = $mysqli->query($query))
        header("Location: index.php?success");
    else
        header("Location: index.php?failure");
}
