from aiogram import types
from buttons import keyboard_create_text_max_length, \
    keyboard_create_text_temperature
from config import dp, bot
from handler_models import Users, Flags
from openai_api_requests import Temperature, MaxLength


@dp.callback_query_handler(text="set_text_max_length")
@dp.callback_query_handler(text="set_text_temperature")
async def text_settings_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    if answer_data == 'set_text_max_length':
        text = "Set text max length"
        keyboard = keyboard_create_text_max_length
    if answer_data == 'set_text_temperature':
        text = "Set text temperature"
        keyboard = keyboard_create_text_temperature
    await bot.send_message(query.from_user.id, text=text, reply_markup=keyboard)


@dp.callback_query_handler(text=[f"set_text_max_length_{i.value}" for i in MaxLength])
async def set_text_max_length_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    for el in MaxLength:
        if answer_data == f'set_text_max_length_{el.value}':
            text = f"Set text max length {el.value}"
            Users[query.from_user.id].text_settings.MaxLength = el.value
            Flags.text_set_max_length = 1
            # print(Users[query.from_user.id].image_settings.Size)
            await bot.delete_message(query.from_user.id, query.message.message_id)
            await bot.send_message(query.from_user.id, text=text)
            # if Flags.text_set_temperature and Flags.set_text_prompt == 0:
            #     await bot.send_message(query.from_user.id, text=f"Chose create text action\n\nPre-set text settings:\n- max length: {Users[query.from_user.id].text_settings.MaxLength}\n- temperature: {Users[query.from_user.id].text_settings.Temperature}", reply_markup=keyboard_create_text)


@dp.callback_query_handler(text=[f"set_text_temperature_{i.value}" for i in Temperature])
async def set_text_temperature_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    for i in Temperature:
        if answer_data == f'set_text_temperature_{i.value}':
            text = f"Set text temperature {i.value}"
            Users[query.from_user.id].text_settings.Temperature = i.value
            Flags.text_set_temperature = 1
            # print(Users[query.from_user.id].image_settings.Quantity)
            await bot.delete_message(query.from_user.id, query.message.message_id)
            await bot.send_message(query.from_user.id, text=text)
            # if Flags.text_set_max_length and Flags.set_text_prompt == 0:
            #     await bot.send_message(query.from_user.id, text=f"Chose create text action\n\nPre-set text settings:\n- max length: {Users[query.from_user.id].text_settings.MaxLength}\n- temperature: {Users[query.from_user.id].text_settings.Temperature}", reply_markup=keyboard_create_text)
