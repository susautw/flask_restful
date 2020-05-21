from flask import Flask
from flask_restful import Api

from app_config import AppConfig
from final_graduation.config import *
from final_graduation.controller import HelloWorld, CategoryItemController
from final_graduation.controller import CategoryController
from final_graduation.kernal import Response
from final_graduation.kernal.bootstrap import Bootstrap


def main():
    app = create_app()
    app.run()


def create_app() -> Flask:
    # load configs
    Bootstrap.bootstrap()
    app_config = Bootstrap.instance().configs['app']
    assert isinstance(app_config, AppConfig)

    app = Flask(__name__)
    api = Api(app)
    Response.set_debug(app_config.debug)
    register_routes(api, app)
    app.debug = app_config.debug
    return app


def register_routes(api: Api, app: Flask):
    api.add_resource(HelloWorld, '/')
    api.add_resource(CategoryController, '/category')
    api.add_resource(CategoryItemController, '/category/<string:category_id>')


if __name__ == '__main__':
    main()
