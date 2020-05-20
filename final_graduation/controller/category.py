from bson import ObjectId
from flask_restful import Resource
from .. import models
from ..kernal import Response


class CategoryController(Resource):
    def get(self):
        res = Response()
        with res:
            # TODO test it can or can't automatically convert to json.
            res.result = list(models.Category.get_all_categories())
        return res


class CategoryItemController(Resource):
    def get(self, category_id: str):
        res = Response()
        with res:
            res.result = models.Category.get_by_id(ObjectId(category_id))
        return res
