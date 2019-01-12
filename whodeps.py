#!/usr/bin/env python3.7

import argparse
import json
import shlex
import subprocess


def arg_parse():
    parser = argparse.ArgumentParser(description="do the revert of brew deps.")
    parser.add_argument("formula_name")
    args = parser.parse_args()
    return args


def main():
    args = arg_parse()
    brew_cmd = "brew info --installed --json"
    result = subprocess.run(shlex.split(brew_cmd), capture_output=True)
    for formula in json.loads(result.stdout):
        if args.formula_name in formula["dependencies"]:
            print(formula["name"])
 

if __name__ == "__main__":
    main()
