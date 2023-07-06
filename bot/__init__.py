from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from telebot import custom_filters
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
storage = StateMemoryStorage()
bot = TeleBot(TOKEN, state_storage=storage)
bot.add_custom_filter(custom_filters.StateFilter(bot))

from . import basic_handlers
from . import history_handlers
