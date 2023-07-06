from . import bot
from .history import Query


@bot.message_handler(commands=['history'])
def history_handler(m):
    res = Query.filter(Query.chat_id == m.chat.id).order_by(Query.time.desc()).limit(10)
    for q in res:
        bot.send_message(m.chat.id, f'{q.type} {q.category} {q.amount}')
