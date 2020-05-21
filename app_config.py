from final_graduation.kernal import config as cfg


class AppConfig(cfg.BaseConfig):
    debug: bool = cfg.Option(default=False, preprocess=cfg.to_bool)
