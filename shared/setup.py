import re
import os
import sys
import shutil
import fileinput


APP_NAME = os.environ["APP_NAME"]
VERSION = os.environ["VERSION"]
PYTHON_VERSION = sys.version.split(' ')[0]


def replace_file_data(filename, rules):
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            is_found = False
            for rule in rules:
                if re.match(rule, line):
                    is_found = True
                    break
            if is_found:
                line = re.sub(rule, rules[rule], line)
            print(line, end="")


def main():
    replace_file_data(
        "pyproject.toml",
        {
            fr"^version.*$": f"version = \"{VERSION}\"",
            fr"^name.*$": f"name = \"{APP_NAME}\"",
            fr"^requires-python.*$": f"requires-python = \">={PYTHON_VERSION}\""
        }
    )
    shutil.move("./src/shared", f"./src/{APP_NAME}")

    os.system("python -m build -w")


if __name__ == "__main__":
    main()
