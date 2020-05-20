from pathlib import Path
from typing import List, Dict

import flower.core.config as cfg


class ConfigMeta(cfg.BaseConfig):
    path: Path = cfg.Option(required=True, preprocess=cfg.to_path)
    method: str = cfg.Option(default='yaml', preprocess=cfg.to_string)
    name: str = cfg.Option(required=True, preprocess=cfg.to_string)

    def __init__(self, meta: Dict):
        super().__init__(cfg.DictConfigLoader(meta))


class BootstrapConfig(cfg.BaseConfig):
    configs: List[ConfigMeta] = cfg.Option(
        required=True, option_type=list, preprocess=lambda li, _: [ConfigMeta(p) for p in li]
    )

