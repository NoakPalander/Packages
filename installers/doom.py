import os
import shutil
import subprocess
from utils import Group


def install(group: Group):
    path = f'{os.getenv("HOME")}/.emacs.d'
    if os.path.isdir(path):
        shutil.rmtree(path)

    os.mkdir(path)
    subprocess.run(f'git clone --depth 1 https://github.com/hlissner/doom-emacs {path}'.split())
    subprocess.run(f'{path}/bin/doom install'.split())
