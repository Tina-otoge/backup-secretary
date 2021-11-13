from pathlib import Path


class Target:
    def __init__(self, path):
        self.path = Path(path).expanduser()

    def __str__(self):
        return str(self.path)

    def get_file(self):
        with open(self.path, 'rb') as f:
            return {self.path.name: f.read()}
