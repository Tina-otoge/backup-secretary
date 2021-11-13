import logging
import time
from pathlib import Path

from .handlers.webhook import WebhookHandler


CONFIG_PATH = Path('./config.json')

from .config import config

def execute_handler():
    handler = WebhookHandler(config)
    handler.execute()

def run():
    delay = None
    if config.get('frequency') == 'weekly':
        delay = 7 * 24 * 60 * 60
    while delay:
        execute_handler()
        if delay:
            logging.info(f'Sleeping for {delay}s')
            time.sleep(delay)
