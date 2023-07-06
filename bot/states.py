from telebot.handler_backends import State, StatesGroup


class BaseStates(StatesGroup):
    type = State()
    category = State()
    amount = State()
    price = State()



