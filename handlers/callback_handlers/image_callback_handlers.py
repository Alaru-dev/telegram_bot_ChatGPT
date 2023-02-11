from aiogram import types
from buttons import keyboard_create_image_size, keyboard_create_image_quantity
from config import dp, bot
from handler_models import Users, Flags
from openai_api_requests import ImageSize, max_image_quantity


@dp.callback_query_handler(text="set_image_size")
@dp.callback_query_handler(text="set_image_quantity")
async def image_settings_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    if answer_data == 'set_image_size':
        text = "Set image size"
        keyboard = keyboard_create_image_size
    if answer_data == 'set_image_quantity':
        text = "Set image quantity"
        keyboard = keyboard_create_image_quantity
    await bot.send_message(query.from_user.id, text=text, reply_markup=keyboard)


@dp.callback_query_handler(text=[f"set_image_size_{el.value}" for el in ImageSize])
async def set_image_size_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    for el in ImageSize:
        if answer_data == f'set_image_size_{el.value}':
            text = f"Set image size {el.value}"
            Users[query.from_user.id].image_settings.Size = el.value
            Flags.image_set_size = 1
            await bot.delete_message(query.from_user.id, query.message.message_id)
            # await bot.edit_message_text(
            #     text=f"Set image prompt {Users[query.from_user.id].image_settings.str_get_settings()}",
            #     chat_id=query.from_user.id, message_id=Users[query.from_user.id].inline_mess_id)
            await bot.send_message(query.from_user.id, text=text)
            # if Flags.image_set_quantity and Flags.set_image_prompt == 0:
            #     await bot.send_message(query.from_user.id, text=f"Chose create image action\n\nPre-set image settings:\n- image quantity: {Users[query.from_user.id].image_settings.Quantity}\n- size: {Users[query.from_user.id].image_settings.Size}", reply_markup=keyboard_create_image)


@dp.callback_query_handler(text=[f"set_image_quantity_{i}" for i in range(1, max_image_quantity+1)])
async def set_image_quantity_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    for i in range(1, max_image_quantity + 1):
        if answer_data == f'set_image_quantity_{i}':
            text = f"Set image quantity {i}"
            Users[query.from_user.id].image_settings.Quantity = i
            Flags.image_set_quantity = 1
            # print(Users[query.from_user.id].image_settings.Quantity)
            await bot.delete_message(query.from_user.id, query.message.message_id)
            # await bot.edit_message_text(text=f"Set image prompt {Users[query.from_user.id].image_settings.str_get_settings()}", chat_id=query.from_user.id, message_id=Users[query.from_user.id].inline_mess_id, reply_markup=keyboard_prompt_image_settings)
            await bot.send_message(query.from_user.id, text=text)

            # if Flags.image_set_size and Flags.set_image_prompt == 0:
            #     await bot.send_message(query.from_user.id, text=f"Chose create image action\n\nPre-set image settings:\n- image quantity: {Users[query.from_user.id].image_settings.Quantity}\n- size: {Users[query.from_user.id].image_settings.Size}", reply_markup=keyboard_create_image)
