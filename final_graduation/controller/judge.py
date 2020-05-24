from bson import ObjectId
from flask_restful import Resource, reqparse

from .. import models
from ..kernal import make_response_all_verbs


@make_response_all_verbs
class JudgeController(Resource):
    def get(self):
        return [judge.to_json() for judge in models.Judge.get_all_judges()]

    def post(self):
        args = self._get_post_req_parser().parse_args()
        judge = models.Judge.create(args['name'])
        judge.save()
        return {
            'inserted_id': str(judge.id)
        }

    @staticmethod
    def _get_post_req_parser():
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        return parser


@make_response_all_verbs
class JudgeItemController(Resource):
    def get(self, judge_id: str):
        return models.Judge.get_by_id(ObjectId(judge_id)).to_json()
