<?php

include "vk_api.php"; 


const VK_KEY = "ec26f81e721b444281bad7a27e1094bf3167d7c2544fde6547d164e0a66c77e30e6926bf80b0461c0f5a4";  // Токен сообщества
const ACCESS_KEY = "987229df";  // Тот самый ключ из сообщества 
const VERSION = "5.81"; // Версия API VK


$vk = new vk_api(VK_KEY, VERSION); 
$data = json_decode(file_get_contents('php://input')); 

if ($data->type == 'confirmation') { 
    exit(ACCESS_KEY); 
}
$vk->sendOK(); 
// ====== Наши переменные ============
$id = $data->object->from_id; // Узнаем ID пользователя, кто написал нам
$message = $data->object->text; // Само сообщение от пользователя
// ====== *************** ============

if ($data->type == 'message_new') {

    if ($message == '!бот') {

            $vk->sendMessage($id, "Привет :-)");
			
        }


	}
	