from typing import Dict, Type, TYPE_CHECKING

from . import BaseConfig
from flower.core import utils, exceptions

if TYPE_CHECKING:
    from . import BaseConfigLoader


class ConfigFactory:
    loaders = None
    suffix: str = "Config"

    @classmethod
    def create_config(cls, config: str, loader: 'BaseConfigLoader') -> 'BaseConfig':
        configs = cls._get_all_configs()
        if config + cls.suffix in configs:
            config += cls.suffix
        elif config[0].capitalize() + config[1:] + cls.suffix in configs:
            config = config[0].capitalize() + config[1:] + cls.suffix
        elif config not in configs:
            raise exceptions.ClassNotFoundException(config)
        return configs[config](loader)

    @classmethod
    def _get_all_configs(cls) -> Dict[str, Type['BaseConfig']]:
        if cls.loaders is not None:
            return cls.loaders
        configs = utils.reflections.find_subclasses(BaseConfig)
        return {
            config.__name__: config for config in configs
        }

    @classmethod
    def get_suffix(cls) -> str:
        return cls.suffix

    @classmethod
    def set_suffix(cls, suffix: str) -> None:
        cls.suffix = suffix
