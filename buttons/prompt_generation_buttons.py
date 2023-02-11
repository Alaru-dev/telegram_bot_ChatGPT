from aiogram import types

keyboard_prompt_generation = types.InlineKeyboardMarkup(row_width=2)

keyboard_prompt_generation.add(
    types.InlineKeyboardButton(text="Create image", callback_data="gen_image_prompt"),
    types.InlineKeyboardButton(text="Create text", callback_data="gen_text_prompt"),
    types.InlineKeyboardButton(text="Create code", callback_data="gen_code_prompt"),
    )

keyboard_prompt_image_settings = types.InlineKeyboardMarkup(row_width=2)
keyboard_prompt_image_settings.add(
    types.InlineKeyboardButton(text="Set image size", callback_data="set_image_size"),
    types.InlineKeyboardButton(text="Set image quantity", callback_data="set_image_quantity"),
    types.InlineKeyboardButton(text="Generate image", callback_data="generate_image"),
)

keyboard_prompt_text_settings = types.InlineKeyboardMarkup(row_width=2)
keyboard_prompt_text_settings.add(
    types.InlineKeyboardButton(text="Set text max length", callback_data="set_text_max_length"),
    types.InlineKeyboardButton(text="Set text temperature", callback_data="set_text_temperature"),
    types.InlineKeyboardButton(text="Generate text", callback_data="generate_text"),
)

keyboard_prompt_code_settings = types.InlineKeyboardMarkup(row_width=2)
keyboard_prompt_code_settings.add(
    types.InlineKeyboardButton(text="Set code max length", callback_data="set_code_max_length"),
    types.InlineKeyboardButton(text="Set code temperature", callback_data="set_code_temperature"),
    types.InlineKeyboardButton(text="Generate code", callback_data="generate_code"),
)
