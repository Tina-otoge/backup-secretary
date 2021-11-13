import logging
import time

from backup_secretary.target import Target


class BaseHandler:
    def __init__(self, config: dict):
        self.targets = map(Target, config.get('paths', []))
        self.config = config.get('handler', {})

    def execute(self):
        delay = self.config.get('delay', 0)
        for target in self.targets:
            logging.debug(f'Running {self.execute_one} on {target}')
            self.execute_one(target)
            if delay:
                logging.info(f'Sleeping for {delay}s before handling next target')
                time.sleep(delay)

    def execute_one(self, _target: Target):
        raise NotImplementedError
