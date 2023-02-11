from aiogram import types
from buttons import keyboard_create_code_max_length, keyboard_create_code_temperature
from config import dp, bot
from handler_models import Users, Flags
from openai_api_requests import Temperature, MaxLength


@dp.callback_query_handler(text="set_code_max_length")
@dp.callback_query_handler(text="set_code_temperature")
async def code_settings_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    if answer_data == 'set_code_max_length':
        text = "Set code max length"
        keyboard = keyboard_create_code_max_length
    if answer_data == 'set_code_temperature':
        text = "Set code temperature"
        keyboard = keyboard_create_code_temperature
    await bot.send_message(query.from_user.id, text=text, reply_markup=keyboard)


@dp.callback_query_handler(text=[f"set_code_max_length_{i.value}" for i in MaxLength])
async def set_code_max_length_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    for el in MaxLength:
        if answer_data == f'set_code_max_length_{el.value}':
            text = f"Set code max length {el.value}"
            Users[query.from_user.id].code_settings.MaxLength = el.value
            Flags.code_set_max_length = 1
            # print(Users[query.from_user.id].image_settings.Size)
            await bot.delete_message(query.from_user.id, query.message.message_id)
            await bot.send_message(query.from_user.id, text=text)
            # if Flags.code_set_temperature and Flags.set_code_prompt == 0:
            #     await bot.send_message(query.from_user.id, text=f"Chose create code action\n\nPre-set code settings:\n- max length: {Users[query.from_user.id].code_settings.MaxLength}\n- temperature: {Users[query.from_user.id].code_settings.Temperature}", reply_markup=keyboard_create_code)


@dp.callback_query_handler(text=[f"set_code_temperature_{i.value}" for i in Temperature])
async def set_code_temperature_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    for i in Temperature:
        if answer_data == f'set_code_temperature_{i.value}':
            text = f"Set code temperature {i.value}"
            Users[query.from_user.id].code_settings.Temperature = i.value
            Flags.code_set_temperature = 1
            # print(Users[query.from_user.id].image_settings.Quantity)
            await bot.delete_message(query.from_user.id, query.message.message_id)
            await bot.send_message(query.from_user.id, text=text)
            # if Flags.code_set_max_length and Flags.set_code_prompt == 0:
            #     await bot.send_message(query.from_user.id, text=f"Chose create code action\n\nPre-set code settings:\n- max length: {Users[query.from_user.id].code_settings.MaxLength}\n- temperature: {Users[query.from_user.id].code_settings.Temperature}", reply_markup=keyboard_create_code)
