from flask import Flask
from flask_restful import Api

from final_graduation.controller import HelloWorld
from final_graduation.kernal import Response


def main():
    debug = True
    app = create_app(debug)
    app.run(debug=debug)


def create_app(debug) -> Flask:
    app = Flask(__name__)
    api = Api(app)
    Response.set_debug(debug)
    register_routes(api, app)
    return app


def register_routes(api: Api, app: Flask):
    api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    main()
