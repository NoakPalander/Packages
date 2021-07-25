import subprocess
from utils import Group


def install(group: Group):
    assert(group.packages is not None and len(group.packages) != 0)
    subprocess.run(f'sudo pacman -S {" ".join(group.packages)}'.split())
