from aiogram import types

from openai_api_requests.func_attributes import MaxLength, Temperature


keyboard_create_text_max_length = types.InlineKeyboardMarkup(row_width=3)
keyboard_create_text_max_length.add(*[types.InlineKeyboardButton(text=f"{i.value}", callback_data=f"set_text_max_length_{i.value}") for i in MaxLength])

keyboard_create_text_temperature = types.InlineKeyboardMarkup(row_width=3)
keyboard_create_text_temperature.add(*[types.InlineKeyboardButton(text=f"{i.value}", callback_data=f"set_text_temperature_{i.value}") for i in Temperature])
