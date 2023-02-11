import logging
import os
from dataclasses import dataclass

import openai
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

load_dotenv()

# API keys
BOT_KEY = os.getenv("BOT_KEY")
AI_KEY = os.getenv("AI_KEY")

# Configure logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_KEY)
dp = Dispatcher(bot)

# Add openai key
openai.api_key = AI_KEY
