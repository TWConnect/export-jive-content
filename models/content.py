from peewee import *
from models.db import db
import json


class Content(Model):
    jive_id = IntegerField(unique=True)
    self_ref = TextField()
    content_id = IntegerField()
    parent_place_id = IntegerField()
    parent = TextField()

    subject = TextField()
    content_text = TextField()
    content_type = TextField()

    tags = TextField()
    categories = TextField()

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
        # if obj['type'] != 'discussion':
        #     print('not discussion')
        #     return

        content = Content(
            jive_id = int(obj['id']),
            self_ref = obj['resources']['self']['ref'],
            parent_place_id = int(obj['parentPlace']['placeID']),
            parent = obj['parent'],
            content_id = int(obj['contentID']),
            subject = obj['subject'],
            content_text = obj['content']['text'],
            content_type = obj['content']['type'],
            author_id = int(obj['author']['id']),
            author_display_name = obj['author']['displayName'],
            tags = json.dumps(obj['tags']),
            categories = json.dumps(obj['tags']) if ('tags' in obj) else "[]",
            status = obj['status'],
            published = obj['published'],
            updated = obj['updated'],
            type = obj['type']
        )

        query = Content.select().where(Content.jive_id == int(obj['id']))
        if not query.exists():
            content.save()

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


db.create_tables([Content], safe=True)
