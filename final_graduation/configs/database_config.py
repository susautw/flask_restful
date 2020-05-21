import mongoengine as mg

from ..kernal import config as cfg


class DatabaseConfig(cfg.BaseConfig):
    host: str = cfg.Option(default='127.0.0.1', preprocess=cfg.to_string)
    port: int = cfg.Option(default=27017, preprocess=cfg.to_integer)
    username: str = cfg.Option(required=True, preprocess=cfg.to_string)
    password: str = cfg.Option(required=True, preprocess=cfg.to_string)
    database: str = cfg.Option(required=True, preprocess=cfg.to_string)

    def post_load(self):
        mg.connect(
            db=self.database,
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port
        )
