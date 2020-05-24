from bson import ObjectId
from flask_restful import Resource

from .. import models
from ..kernal import make_response_all_verbs
from flask_restful import reqparse


@make_response_all_verbs
class CategoryController(Resource):
    def get(self, response):
        response.result = [category.to_json() for category in models.Category.get_all_categories()]

    def post(self, response):
        args = self._get_post_req_parser().parse_args()
        parent_id = args['parent']
        parent = models.Category.get_by_id(ObjectId(parent_id)) if parent_id is not None else None
        category = models.Category.create(args['name'], args['description'], parent)
        category.save()
        response.result = {
            'inserted_id': str(category.id)
        }

    @staticmethod
    def _get_post_req_parser():
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('parent', type=str, default=None, nullable=True)
        return parser


@make_response_all_verbs
class CategoryItemController(Resource):
    def get(self, response, category_id: str):
        response.result = models.Category.get_by_id(ObjectId(category_id)).to_json()
