from . import bot
from .keyboards import create_categories_keyboard
from .history import Query
from .api import get_products_of_category, get_all_categories
from .helpers import create_text
from .states import BaseStates


@bot.message_handler(commands=['low', 'high', 'custom'])
def basic_handler(m):
    bot.set_state(m.from_user.id, BaseStates.type, m.chat.id)
    with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
        if m.text == '/low':
            bot.send_message(m.chat.id, 'Выборка товаров с низкой ценой.Выберите категорию',
                             reply_markup=create_categories_keyboard())
            data['type'] = '/low'
            bot.set_state(m.from_user.id, BaseStates.category, m.chat.id)

        elif m.text == '/high':
            bot.send_message(m.chat.id, 'Выборка товаров с высокой ценой.Выберите категорию',
                             reply_markup=create_categories_keyboard())
            data['type'] = '/high'
            bot.set_state(m.from_user.id, BaseStates.category, m.chat.id)

        elif m.text == '/custom':
            bot.send_message(m.chat.id, 'Вы выбрали кастомную филь-цию,укажите диапазон цен.')
            data['type'] = '/custom'
            bot.set_state(m.from_user.id, BaseStates.price, m.chat.id)


@bot.message_handler(state=BaseStates.price)
def price_range_handler(m):
    with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
        try:
            p1, p2 = m.text.split('-')
            data['from_price'] = int(p1)
            data['to_price'] = int(p2)
            bot.send_message(m.chat.id, f'Вы выбрали товары с ценами от {p1} до {p2},выберите категорию.',
                             reply_markup=create_categories_keyboard())
            bot.set_state(m.from_user.id, BaseStates.category, m.chat.id)
        except:
            bot.send_message(m.chat.id, 'Вы указали не правильно диапазон цен!')
            return


@bot.message_handler(state=BaseStates.category)
def category_handler(m):
    if m.text not in get_all_categories():
        bot.send_message(m.chat.id, 'Вы указали не верную категорию')
        return
    with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
        data['category'] = m.text
    bot.send_message(m.chat.id, f'Вы выбрали категорию: {m.text}. Укажите кол-во товаров.')
    bot.set_state(m.from_user.id, BaseStates.amount, m.chat.id)


@bot.message_handler(state=BaseStates.amount)
def amount_handler(m):
    if not m.text.isdigit():
        bot.send_message(m.chat.id, 'Вы ввели не число')
        return
    amount = int(m.text)
    with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
        data['amount'] = amount
        products = get_products_of_category(data['category'])
        if data['type'] == '/low':
            products.sort(key=lambda x: x['price'])

        elif data['type'] == '/high':
            products.sort(key=lambda x: x['price'], reverse=True)

        elif data['type'] == '/custom':
            products = list(filter(
                lambda p: data['from_price'] <= p['price'] <= data['to_price'], products))

        products = products[0:amount]
        for p in products:
            bot.send_photo(m.chat.id, p['thumbnail'], create_text(p['title'], p['description'], p['price']))

        q = Query(
            chat_id=m.chat.id,
            category=data['category'],
            type=data['type'],
            amount=data['amount']
        )
        if data['type'] == '/custom':
            q.from_price = data['from_price']
            q.to_price = data['to_price']

        q.save()

    bot.delete_state(m.from_user.id, m.chat.id)
