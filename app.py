from flask import Flask
from flask_restful import Api

from app_config import AppConfig
from final_graduation.controller import HelloWorld
from final_graduation.controller import CategoryController
from final_graduation.kernal import Response
from final_graduation.kernal.bootstrap import Bootstrap


def main():
    # load configs
    Bootstrap.bootstrap()
    app_config = Bootstrap.instance().configs['app']
    assert isinstance(app_config, AppConfig)
    app = create_app(app_config)
    app.run(debug=app_config.debug)


def create_app(config: AppConfig) -> Flask:
    app = Flask(__name__)
    api = Api(app)
    Response.set_debug(config.debug)
    register_routes(api, app)
    return app


def register_routes(api: Api, app: Flask):
    api.add_resource(HelloWorld, '/')
    api.add_resource(CategoryController, '/category')


if __name__ == '__main__':
    main()
