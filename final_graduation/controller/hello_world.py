from flask_restful import Resource

from final_graduation.kernal.response import Response


class HelloWorld(Resource):
    def get(self):
        res = Response()
        with res:
            res.result = {'hello': None}
            # raise TypeError('s')
        return res
