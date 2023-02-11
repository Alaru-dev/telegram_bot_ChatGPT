from datetime import datetime

from aiogram import types
from buttons import keyboard_prompt_generation
from config import dp, logging, bot
from handler_models import User, Users


@dp.message_handler(commands=['start'])
async def send_wellcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    logging.info(f'Start conversation chat:{message.chat}, user_id:{message.from_user.id}, user_name:{message.from_user.username}')
    await bot.send_message(message.chat.id, text=f"Hi! {message.chat.username}\nI'm ChatGPT Bot!\nPowered by aiogram, openai, deep_translator.\nAlaru-dev\n\n Just write description and chose action") #, reply_markup=base_keyboard_start


@dp.message_handler()
async def create_generator_(message: types.Message):
    logging.info(f'{str(datetime.now())} chat:{message.chat}, user_id:{message.from_user.id}, user_name:{message.from_user.username} get create request {message.text}')
    Users[message.chat.id] = User
    Users[message.chat.id].message = message
    await message.answer(
        f"{message.chat.username} chose generation action\n{message.text}",
        reply_markup=keyboard_prompt_generation)
