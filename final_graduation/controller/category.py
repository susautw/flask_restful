from bson import ObjectId
from flask_restful import Resource
from .. import models
from ..kernal import Response
from flask_restful import reqparse


class CategoryController(Resource):
    def get(self):
        res = Response()
        with res:
            # TODO test it can or can't automatically convert to json.
            res.result = list(models.Category.get_all_categories())
        return res

    def post(self):
        res = Response()
        with res:
            args = self._get_post_req_parser().parse_args()
            parent = models.Category.get_by_id(ObjectId(args['parent']))
            category = models.Category.create(args['name'], args['description'], parent)
            category.save()
            res.result = {
                'inserted_id': category.id
            }
        return res

    @staticmethod
    def _get_post_req_parser():
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('parent', type=str, default=None, nullable=True)
        return parser


class CategoryItemController(Resource):
    def get(self, category_id: str):
        res = Response()
        with res:
            res.result = models.Category.get_by_id(ObjectId(category_id))
        return res
