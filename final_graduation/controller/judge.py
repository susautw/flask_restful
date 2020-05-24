from bson import ObjectId
from flask_restful import Resource

from .. import models
from ..kernal import make_response_all_verbs


@make_response_all_verbs
class JudgeController(Resource):
    def get(self, response):
        response.result = [judge.to_json() for judge in models.Judge.get_all_judges()]


@make_response_all_verbs
class JudgeItemController(Resource):
    def get(self, response, judge_id: str):
        response.result = models.Judge.get_by_id(ObjectId(judge_id))
