import importlib
import json
import os
from typing import List
import sys
import subprocess
from utils import Group


def load_config(file: str) -> List[Group]:
    with open(file, 'r') as reader:
        data = json.loads('\n'.join(reader.readlines()))
        return [Group(**item) for item in data]


def main():
    if len(sys.argv) > 1:
        groups = load_config(sys.argv[1])
    else:
        groups = load_config('packages.json')

    for group in groups:
        print(f'[TASK; {group.name}]')
        assert(group.script is not None or group.command is not None)

        # Run the command immediately
        if group.command is not None:
            print(group.command)
            subprocess.run(group.command.split())

        if group.script is not None:
            assert(os.path.isfile(group.script))
            mod = importlib.import_module(group.script.replace('/', '.').replace('.py', ''))
            try:
                mod.install(group)
            except AttributeError:
                print(f'Invalid installer, missing an appropriate "install" function')


if __name__ == '__main__':
    main()
