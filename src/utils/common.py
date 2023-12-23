from __future__ import annotations

import logging
import sys

import yaml
from yaml.loader import SafeLoader

from src.utils.constants import CONFIG_FILE
from src.utils.constants import LOGGING_FORMAT

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(LOGGING_FORMAT)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

conf: dict = {}


def config() -> dict:
    """
    Loads the config.yaml file and returns a dict
    stored in config
    Returns:
        dict: configuration dictionary
    """

    global conf
    if not conf:
        with open(CONFIG_FILE, encoding="utf-8") as cfg:
            conf = yaml.load(cfg, Loader=SafeLoader)
        logger.log(logging.INFO, "Config loaded")
    return conf
