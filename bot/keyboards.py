from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from .api import get_all_categories


def create_categories_keyboard():
    keys = ReplyKeyboardMarkup(one_time_keyboard=True)
    categories = get_all_categories()
    for i in categories:
        b = KeyboardButton(i)
        keys.add(b)

    return keys
