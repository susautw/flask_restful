from typing import Iterator

import mongoengine as mg
from bson import ObjectId

from final_graduation.exceptions.no_data_found import NoDataFound


class Judge(mg.Document):
    name: str = mg.StringField(max_length=50)

    meta = {
        'indexes': [
            '#name',
            'name',
            '-name'
        ]
    }

    @classmethod
    def get_all_judges(cls) -> Iterator['Judge']:
        return cls.objects()

    @classmethod
    def get_by_id(cls, obj_id: ObjectId) -> 'Judge':
        query = cls.objects(id=obj_id)
        if query.count() == 0:
            raise NoDataFound(f'category={obj_id}')
        return query[0]
