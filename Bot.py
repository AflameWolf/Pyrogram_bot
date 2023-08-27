import os
from pyrogram import Client
from pyrogram.enums import ChatAction
from pyrogram.types import Message,InputMediaPhoto
from pyrogram import filters
import time
from controllers import *
from loguru import logger


logger.add("massage.log", format="{time} {level} {message}", level="INFO", rotation="10kb", compression="zip")


api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")


client = Client(name="my_client", api_id=api_id, api_hash=api_hash)

minutes=60


async def filter_admin(_, __, message):
    return message.text =="/users_today"

filter_admin = filters.create(filter_admin)


@client.on_message(filters=filter_admin)
async def all_message(client:Client, message: Message):
    """Отлавливем сообщения от админа и возвращаем количество зареганых людей"""
    cl= get_today_clients_count()
    await client.send_message("me",str(cl))

photo = InputMediaPhoto("./photo.jpg")

@client.on_message()
async def admin_message(client:Client, message: Message):
    """Отлавливем все входящие сообщения и делаем воронку"""
    if create_client_if_not_exists(message.chat.id) == True:

        await send_message_with_delay(message.chat.id,"Добрый день!",10)
        logger.info("Сообщение доставлено:Добрый день!")

        await send_message_with_delay(message.chat.id, "Подготовила для вас материал",90)
        logger.info("Сообщение доставлено:Подготовила для вас материал")

        await client.send_photo(message.chat.id, "./photo.jpg")
        logger.info("Сообщение доставлено:Фото")
        time.sleep(minutes*120)

        if client.search_messages(message.id,"TRIGGER"):
            logger.info("Найден триггер!")
            return
        await send_message_with_delay(message.chat.id, "Скоро вернусь с новым материалом!", 0)

    else:
        await client.send_message(message.chat.id, "Вы уже есть в базе")



async def send_message_with_delay(massage_cat_id,send_mes,time_wait):
    time.sleep(minutes * time_wait)
    await client.send_chat_action(massage_cat_id, ChatAction.TYPING)  # Имитируем что пишем от руки
    time.sleep(5)
    await client.send_message(massage_cat_id, send_mes)
