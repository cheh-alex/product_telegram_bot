
from peewee import SqliteDatabase, CharField,IntegerField,DateTimeField, Model
from datetime import datetime

connection = SqliteDatabase('history.db')


class Query(Model):
    chat_id = CharField(max_length=100, null=False)
    category = CharField(max_length=100, null=False)
    type = CharField(max_length=50, null=False)
    time = DateTimeField(default=datetime.utcnow())
    amount = IntegerField()
    from_price = IntegerField(null=True)
    to_price = IntegerField(null=True)

    class Meta:
        database = connection
        db_table = 'Queries'


Query.create_table()
