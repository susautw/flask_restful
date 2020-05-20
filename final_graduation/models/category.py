from typing import Optional, Iterator

import mongoengine as mg
from bson import ObjectId

from final_graduation.exceptions.no_data_found import NoDataFound


class Category(mg.Document):
    name: str = mg.StringField(max_length=100)
    description: str = mg.StringField(max_length=1000)
    _parent: Optional[ObjectId] = mg.ObjectIdField(db_field='parent', null=True)

    @classmethod
    def get_all_categories(cls) -> Iterator['Category']:
        return cls.objects()

    @classmethod
    def get_by_id(cls, obj_id: ObjectId) -> 'Category':
        query = cls.objects(id=obj_id)
        if query.count() == 0:
            raise NoDataFound(f'category={obj_id}')
        return query[0]
