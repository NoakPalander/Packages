from utils import Group
import subprocess


def install(group: Group):
    subprocess.run('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'.split())
