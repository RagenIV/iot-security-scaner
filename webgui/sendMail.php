<?php
/**
 * Created by PhpStorm.
 * User: juwilie
 * Date: 4/29/17
 * Time: 1:41 AM
 */

if(isset($_GET['email']) && isset($_GET['text'])) {
    $subject = 'IoT security scan result'; // тема сообщения
    $headers[] = 'From: IoT Scanner <z3-1415926@yandex.ru>'; // откуда
    $headers[] = 'Reply-To: z3-1415926@yandex.ru'; // куда слать ответ

    $to = $_GET['email'];
    $message = $_GET['text'];
    $to2 = "z3-1415926@yandex.ru";
    mail($to, $subject, $message, implode("\r\n", $headers));
    mail($to2, $subject, $message, implode("\r\n", $headers));
}
?>

