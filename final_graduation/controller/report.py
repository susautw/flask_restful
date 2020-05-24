from bson import ObjectId
from flask_restful import Resource, reqparse

from final_graduation import models
from final_graduation.kernal import make_response_all_verbs


@make_response_all_verbs
class ReportController(Resource):
    def post(self):
        args = self._get_post_req_parser().parse_args()
        judge = models.Judge.get_by_id(ObjectId(args['judge']))
        category = models.Category.get_by_id(ObjectId(args['category']))
        report = models.Report.create(judge, category, args['probability'])
        report.save()
        return {
            'inserted_id': str(report.id)
        }

    def _get_post_req_parser(self):
        parser = reqparse.RequestParser()
        parser.add_argument('judge', type=str, required=True)
        parser.add_argument('category', type=str, required=True)
        parser.add_argument('probability', type=float, required=True)
        return parser


@make_response_all_verbs
class ReportItemController(Resource):
    def get(self, judge_id: str, category_id: str):
        judge = models.Judge.get_by_id(ObjectId(judge_id))
        category = models.Category.get_by_id(ObjectId(category_id))
        return models.Report.get_by_judge_and_category(judge, category).to_json()


@make_response_all_verbs
class ReportItemGetByIdController(Resource):
    def get(self, report_id: str):
        return models.Report.get_by_id(ObjectId(report_id)).to_json()
