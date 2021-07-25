import shutil
import uuid
import os


class TempDir:
    def __init__(self):
        self.name = f'.{uuid.uuid1().hex}'

    def __enter__(self):
        print(f'[Creating temporary directory {self.name}]\n')
        os.mkdir(self.name)
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(self.name)
        print(f'[Cleaning up {self.name}]\n')
