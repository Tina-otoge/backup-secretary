import json

from . import CONFIG_PATH

with open(CONFIG_PATH) as f:
    config = json.load(f)
