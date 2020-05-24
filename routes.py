from final_graduation.controller import *
__slot__ = ['routes']
routes = {
    CategoryController: '/category',
    CategoryItemController: '/category/<string:category_id>',
    JudgeController: '/judge',
    JudgeItemController: '/judge/<string:judge_id>',
    ReportController: '/report',
    ReportItemController: '/report/<string:judge_id>/<string:category_id>',
    ReportItemGetByIdController: '/report/<string:report_id>'
}
