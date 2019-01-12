#!/usr/bin/env python3.7

import json
import shlex
import subprocess
import sys


def main():
    brew_cmd = "brew info --installed --json"
    result = subprocess.run(shlex.split(brew_cmd), capture_output=True)
    for formula in json.loads(result.stdout):
        if sys.argv[1] in formula["dependencies"]:
            print(formula["name"])
 

if __name__ == "__main__":
    main()
