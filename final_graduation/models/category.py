from typing import Optional, Iterator

import mongoengine as mg
from bson import ObjectId

from final_graduation.exceptions.no_data_found import NoDataFound
from final_graduation.kernal import Model


class Category(Model):
    name: str = mg.StringField(max_length=100)
    description: str = mg.StringField(max_length=1000)
    _parent: Optional[ObjectId] = mg.ObjectIdField(db_field='parent', null=True)

    meta = {
        'indexes': [
            '#name',
            ('name', 'description'),
            '_parent'
        ]
    }

    @classmethod
    def create(cls, name: str, description: str, parent: Optional['Category']) -> 'Category':
        obj_id = parent.id if parent is not None else None
        return cls(
            name=name,
            description=description,
            _parent=obj_id
        )

    @classmethod
    def get_all_categories(cls) -> Iterator['Category']:
        return cls.objects()

    @classmethod
    def get_by_id(cls, obj_id: ObjectId) -> 'Category':
        query = cls.objects(id=obj_id)
        if query.count() == 0:
            raise NoDataFound(f'category={obj_id}')
        return query[0]
