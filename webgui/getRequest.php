<?php
/**
 * Created by PhpStorm.
 * User: juwilie
 * Date: 4/29/17
 * Time: 1:24 AM
 */
include "db.php";

    $query = "SELECT * FROM `requests` WHERE `checked`=0 LIMIT 1";
    if($res = $mysqli->query($query)) {
        $arr = $res->fetch_assoc();

        $resp = array(
            'host' => $arr['hostname'],
            'email' => $arr['email'],
            'adv' => $arr['adv']
        );

        echo json_encode($resp);

        $query = "UPDATE `requests` SET `checked`=1 WHERE `id`=".$arr['id'];
        $res  = $mysqli->query($query);
    }
?>