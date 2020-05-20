from pathlib import Path
from typing import Dict

from .. import config as cfg
from .bootstrap_config import BootstrapConfig


class Bootstrap:
    config_factory = cfg.ConfigLoaderFactory()
    bootstrap_config: BootstrapConfig
    configs: Dict[str, cfg.BaseConfig] = {}
    _instance: 'Bootstrap' = None

    def __init__(self, path: Path, method: str):
        loader = self.config_factory.create_loader(method)
        loader.path = path
        self.bootstrap_config = BootstrapConfig(loader)
        self._load_configs()

    @classmethod
    def bootstrap(cls, path: Path = Path('./configs/bootstrap.yaml'), method: str = 'yaml'):
        cls._instance = cls(path, method)

    def _load_configs(self) -> None:
        for meta in self.bootstrap_config.configs:
            loader = cfg.ConfigLoaderFactory.create_loader(meta.method)
            if not isinstance(loader, cfg.PathBasedConfigLoader):
                raise TypeError(f'Loader should be instance of PathBasedConfigLoader')
            loader.path = meta.path

            config = cfg.ConfigFactory.create_config(meta.name, loader)
            config.post_load()
            self.configs[meta.name] = config

    @classmethod
    def instance(cls) -> 'Bootstrap':
        if cls._instance is None:
            raise Exception('Can\'t get instance before bootstrap.')
        return cls._instance
