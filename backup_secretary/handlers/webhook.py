from datetime import datetime
import json
import logging
import requests

from backup_secretary.target import Target
from . import BaseHandler


class WebhookHandler(BaseHandler):
    def __init__(self, config: dict):
        super().__init__(config)
        self.url = self.config['url']

    def execute_one(self, target: Target):
        data = {
            'content': f'Your backup from {datetime.now()} for {target}',
        } | self.config.get('data', {})
        files = {
            'payload_json': (None, json.dumps(data)),
        } | target.get_file()
        response = requests.post(self.url, files=files)
        logging.debug(response)
