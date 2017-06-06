from models.message import Message
from models.comment import Comment
from models.content import Content


messages = Message.select().order_by(Message.id)

comments = Comment.select().order_by(Comment.id)

contents = Content.select().order_by(Content.id)

for message in messages:
    print (str(message))

for comment in comments:
    print(str(comment))

for content in contents:
    print(str(content))