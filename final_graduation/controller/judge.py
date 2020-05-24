from bson import ObjectId
from flask_restful import Resource

from .. import models
from ..kernal import make_response_all_verbs


@make_response_all_verbs
class JudgeController(Resource):
    def get(self):
        return [judge.to_json() for judge in models.Judge.get_all_judges()]

    def post(self, response):
        pass


@make_response_all_verbs
class JudgeItemController(Resource):
    def get(self, judge_id: str):
        return models.Judge.get_by_id(ObjectId(judge_id))
