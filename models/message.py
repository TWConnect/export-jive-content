from peewee import *
from models.db import db
import json


class Message(Model):
    jive_id = IntegerField(unique=True)
    self_ref = TextField()
    parent_place_id = IntegerField()
    parent = TextField()

    content_text = TextField()
    content_type = TextField()

    tags = TextField()

    author_id = IntegerField()
    author_display_name = TextField()

    status = CharField()

    published = DateTimeField()
    updated = DateTimeField()

    type = CharField()

    class Meta:
        database = db

    @staticmethod
    def parse_response(obj):
        if obj['type'] != 'message':
            print('not message')
            return

        discussion = Message(
            jive_id = int(obj['id']),
            self_ref = obj['resources']['self']['ref'],
            parent_place_id = int(obj['parentPlace']['placeID']),
            parent = obj['parent'],
            content_text = obj['content']['text'],
            content_type = obj['content']['type'],
            tags = json.dumps(obj['tags']),
            author_id = int(obj['author']['id']),
            author_display_name = obj['author']['displayName'],
            status = obj['status'],
            published = obj['published'],
            updated = obj['updated'],
            type = obj['type']
        )

        query = Message.select().where(Message.jive_id == int(obj['id']))
        if not query.exists():
            discussion.save()

    def __str__(self):
        return json.dumps({
            'jive_id': self.jive_id,
            'resources': {
                'self': {
                    'ref': self.self_ref
                }
            },
            'parentPlace': {
                'placeID': self.parent_place_id
            },
            'parent': self.parent,
            'content':{
                'text': self.content_text,
                'type': self.content_type
            },
            'tags': json.loads(self.tags),
            'author': {
                'id': self.author_id,
                'displayName': self.author_display_name
            },
            'status': self.status,
            'published': str(self.published),
            'updated': str(self.updated),
            'type': self.type
        })

db.create_tables([Message], safe=True)
