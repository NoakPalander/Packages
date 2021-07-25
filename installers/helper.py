import subprocess
from utils import Group, TempDir


def install(group: Group):
    with TempDir() as directory:
        subprocess.run(f'git clone https://aur.archlinux.org/yay.git {directory}'.split())
        subprocess.run('makepkg -si'.split(), cwd=directory)
