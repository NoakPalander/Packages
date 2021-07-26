from utils import Group
import os
import subprocess
import sys


def install(group: Group):
    if os.geteuid() == 0:
        with open('/etc/doas.conf', 'w') as writer:
            writer.write('permit :wheel\n')
    else:
        subprocess.run(f'sudo python3 {sys.argv[0]}'.split())
