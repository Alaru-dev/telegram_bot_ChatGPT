import asyncio
from aiogram import types
from deep_translator import GoogleTranslator
from datetime import datetime
from buttons import keyboard_prompt_image_settings, \
    keyboard_prompt_text_settings, keyboard_prompt_code_settings
from config import dp, bot, logging
from handler_models import Users, Flags
from openai_api_requests import create_code, create_image, create_text
from set_messages import prompt_gen_callback_answers


@dp.callback_query_handler(text=prompt_gen_callback_answers)
async def prompt_gen_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    prompt = GoogleTranslator(source='auto', target='en').translate(text=Users[query.from_user.id].message.text)

    if answer_data == "gen_image_prompt":
        Flags.set_image_prompt = 1
        Users[query.from_user.id].image_settings.Prompt = prompt
        text = f"Set image prompt {Users[query.from_user.id].image_settings.str_get_settings()}"
        keyboard = keyboard_prompt_image_settings

    if answer_data == "gen_text_prompt":
        Flags.set_text_prompt = 1
        Users[query.from_user.id].text_settings.Prompt = prompt
        text = f"Set text prompt {Users[query.from_user.id].text_settings.str_get_settings()}"
        keyboard = keyboard_prompt_text_settings

    if answer_data == "gen_code_prompt":
        Flags.set_code_prompt = 1
        Users[query.from_user.id].code_settings.Prompt = prompt
        text = f"Set code prompt {Users[query.from_user.id].code_settings.str_get_settings()}"
        keyboard = keyboard_prompt_code_settings

    message = await bot.send_message(query.from_user.id, text=text, reply_markup=keyboard)
    # print(message)
    # Users[query.from_user.id].inline_mess_id = message.message_id
    await query.message.edit_reply_markup()
    # if answer_data == 'text_prompt':
    #     text = "Start your next message with /tprompt\nit will accepted as prompt for create text"
    #     await bot.send_message(query.from_user.id, text=text)
    #     await query.message.edit_reply_markup()


@dp.callback_query_handler(text="generate_image")
async def prompt_gen_image_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    if answer_data == 'generate_image':
        logging.info(f'{str(datetime.now())} from {query.from_user.username} get create image request {Users[query.from_user.id].image_settings.Prompt}')
        # await query.message.edit_reply_markup()
        await bot.send_message(query.from_user.id,
            text=f"Accepted description:\n\n{Users[query.from_user.id].image_settings.Prompt}\n\nAwait for image generation, could take several minutes")
        image_urls = create_image(**Users[query.from_user.id].image_settings.to_dict())
        # print(image_urls)
        # Wait a little...
        await asyncio.sleep(0.1)
        # Good bots should send chat actions...
        await types.ChatActions.upload_photo()
        # Create media group
        media = types.MediaGroup()
        # # Attach local file
        for image_url in image_urls:
            media.attach_photo(image_url)
        await Users[query.from_user.id].message.reply_media_group(media=media)


@dp.callback_query_handler(text="generate_text")
async def prompt_gen_text_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    if answer_data == 'generate_text':
        logging.info(
            f'{str(datetime.now())} from {query.from_user.username} get create text request {Users[query.from_user.id].text_settings.Prompt}')
        # await query.message.edit_reply_markup()
        await bot.send_message(query.from_user.id, text=f"Accepted description:\n\n{Users[query.from_user.id].text_settings.Prompt}\n\nAwait for text generation, could take several minutes")
        text = create_text(**Users[query.from_user.id].text_settings.to_dict())
        await asyncio.sleep(0.1)
        # Good bots should send chat actions...
        await types.ChatActions.typing()
        logging.info(f'{str(datetime.now())} created text for {query.from_user.username} text: {text}')

        await bot.send_message(query.from_user.id, text=f"English:\n\n{text}")

        text = GoogleTranslator(source='auto', target='uk').translate(
            text=text)
        await bot.send_message(query.from_user.id, text=f"Ukr:\n\n{text}")


@dp.callback_query_handler(text="generate_code")
async def prompt_gen_code_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    if answer_data == 'generate_code':
        logging.info(
            f'{str(datetime.now())} from {query.from_user.username} get create code request {Users[query.from_user.id].code_settings.Prompt}')
        # await query.message.edit_reply_markup()
        await bot.send_message(query.from_user.id, text=f"Accepted description:\n\n{Users[query.from_user.id].code_settings.Prompt}\n\nAwait for code generation, could take several minutes")
        code = create_code(**Users[query.from_user.id].code_settings.to_dict())
        await asyncio.sleep(0.1)
        # Good bots should send chat actions...
        await types.ChatActions.typing()
        logging.info(f'{str(datetime.now())} created code for {query.from_user.username} code: {code}')
        await bot.send_message(query.from_user.id, text=f"{code}")

