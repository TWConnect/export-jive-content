from peewee import *
import datetime

# example for peewee model

psql_db = PostgresqlDatabase('jive', user='postgres', password='postgres')

class User1024(Model):
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = psql_db

if __name__ == "__main__":
    psql_db.create_tables([User1024], safe=True)
    userA = User1024(message="world")
    userA.save()
