import mongoengine as mg
from bson import ObjectId

from . import Judge, Category
from ..exceptions.item_already_exists import ItemAlreadyExists
from ..exceptions.no_data_found import NoDataFound
from ..kernal import Model


class Report(Model):
    judge: Judge = mg.ReferenceField(Judge)
    category: Category = mg.ReferenceField(Category)
    probability: float = mg.FloatField(max_value=1.0, min_value=0.0)

    meta = {
        'indexes': [
            ('judge', 'category'),
            "probability",
            "-probability"
        ]
    }

    @classmethod
    def create(cls, judge: Judge, category: Category, probability: float) -> 'Report':
        if cls._is_report_exists(judge, category):
            raise ItemAlreadyExists(cls.__name__)
        return cls(
            judge=judge,
            category=category,
            probability=probability
        )

    @classmethod
    def get_by_judge_and_category(cls, judge: Judge, category: Category) -> 'Report':
        query: mg.QuerySet = cls.objects(judge=judge, category=category)
        if query.count() == 0:
            raise NoDataFound(f'judge={judge.id} and category={category.id}')
        return query[0]

    @classmethod
    def get_by_id(cls, report_id: ObjectId) -> 'Report':
        query = cls.objects(id=report_id)
        if query.count() == 0:
            raise NoDataFound(f'report={report_id}')
        return query[0]

    @classmethod
    def _is_report_exists(cls, judge: Judge, category: Category) -> bool:
        try:
            cls.get_by_judge_and_category(judge, category)
            return True
        except NoDataFound:
            return False
