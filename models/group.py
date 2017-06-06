from peewee import *
from models.db import db

class SocialGroup(Model):
    jive_id = IntegerField()
    place_id = IntegerField(unique=True)
    self_ref = TextField()

    description = TextField()
    display_name = TextField()
    group_name = TextField()
    
    type = CharField()
    group_type = CharField()
    group_type_v2 = CharField()

    status = CharField()

    created_date = DateTimeField()
    class Meta:
        database = db

    @staticmethod
    def parse_response(obj):
        if obj['type'] != 'group':
            # print('not social group')
            return

        group = SocialGroup(jive_id = int(obj['id']),
                      place_id = int(obj['placeID']),
                      self_ref = obj['resources']['self']['ref'],
                      description = obj['description'],
                      display_name = obj['displayName'],
                      group_name = obj['name'],
                      type = obj['type'],
                      group_type = obj['groupType'],
                      group_type_v2 = obj['groupTypeV2'],
                      status = obj['status'],
                      created_date = obj['published']
                      )
        query = SocialGroup.select().where(SocialGroup.place_id == int(obj['placeID']))
        if not query.exists():
            group.save()

        # print(group.display_name )

db.create_tables([SocialGroup], safe=True)
