from __future__ import annotations

import os


# Directories
UTILS_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.dirname(UTILS_DIR)
ROOT_DIR = os.path.dirname(SOURCE_DIR)

# Files
CONFIG_FILE = os.path.join(ROOT_DIR, "config.yaml")

# Logging
LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
