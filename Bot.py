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
    cl= get_today_client()
    await client.send_message("me",str(cl))

photo = InputMediaPhoto("./photo.jpg")

@client.on_message()
async def all_message(client:Client,message: Message):
    """Отлавливем все входящие сообщения и делаем воронку"""
    if check_client(message.chat.id) == True:

        time.sleep(minutes*10)
        await client.send_chat_action(message.chat.id,ChatAction.TYPING)  # Имитируем что пишем от руки
        time.sleep(5)
        await client.send_message(message.chat.id,"Добрый день!")
        logger.info("Сообщение доставлено:Добрый день!")
        time.sleep(minutes*90)
        await client.send_chat_action(message.chat.id,ChatAction.TYPING)  # Имитируем что пишем от руки
        time.sleep(5)
        await client.send_message(message.chat.id, "Подготовила для вас материал")
        logger.info("Сообщение доставлено:Подготовила для вас материал")
        await client.send_photo(message.chat.id, "./photo.jpg")
        logger.info("Сообщение доставлено:Фото")
        time.sleep(minutes*120)
        if client.search_messages(message.id,"TRIGGER"):
            logger.info("Найден триггер!")
        else:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)  # Имитируем что пишем от руки
            time.sleep(5)
            await client.send_message(message.chat.id, "Скоро вернусь с новым материалом!")
    else:
        await client.send_message(message.chat.id, "Вы уже есть в базе")



