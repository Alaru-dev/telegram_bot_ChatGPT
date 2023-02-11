from aiogram import types

from openai_api_requests.func_attributes import max_image_quantity, ImageSize


keyboard_create_image_size = types.InlineKeyboardMarkup(row_width=3)
keyboard_create_image_size.add(*[types.InlineKeyboardButton(text=f"{i.value}", callback_data=f"set_image_size_{i.value}") for i in ImageSize])

keyboard_create_image_quantity = types.InlineKeyboardMarkup(row_width=3)
keyboard_create_image_quantity.add(*[types.InlineKeyboardButton(text=f"{i}", callback_data=f"set_image_quantity_{i}") for i in range(1, max_image_quantity+1)])
