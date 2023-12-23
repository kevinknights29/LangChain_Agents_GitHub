from __future__ import annotations

import logging
import sys

import yaml
from yaml.loader import SafeLoader

from src.utils.constants import CONFIG_FILE
from src.utils.constants import LOGGING_FORMAT


def create_logger(logger_name: str, level: int = logging.INFO, fmt: str = LOGGING_FORMAT) -> logging.Logger:
    """
    Creates and configures a logger object.

    Args:
        logger_name (str): The name of the logger.
        level (int): The log level to use (default: logging.INFO).
        fmt (str): The format string to use for the logger (default: LOGGING_FORMAT).

    Returns:
        logging.Logger: The configured logger object.
    """
    if logger_name in create_logger.loggers:
        return create_logger.loggers[logger_name]

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    formatter = logging.Formatter(fmt)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    create_logger.loggers[logger_name] = logger
    return logger


def config() -> dict:
    """
    Loads the config.yaml file and returns a dict stored in config.

    Returns:
        dict: configuration dictionary
    """
    if not hasattr(config, "_config"):
        # Configuration has not been loaded yet, so load it
        conf = {}
        with open(CONFIG_FILE, encoding="utf-8") as cfg:
            conf = yaml.load(cfg, Loader=SafeLoader)
        setattr(config, "_config", conf)
        create_logger(__name__).log(logging.INFO, "Config loaded")

    return getattr(config, "_config")


# Initialize the loggers dictionary
create_logger.loggers = {}
