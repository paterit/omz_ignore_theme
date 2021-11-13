import os
import sys
import re


# Extend section ZSH_THEME_RANDOM_IGNORED in the .zshrc file with theme names
def add_ignored_theme_to_zshrc(new_ignored_theme_name):
    ignored_theme_names = []
    zshrc_path = os.path.expanduser("~/.zshrc_bak")
    with open(zshrc_path, "r") as zshrc_file:
        all = zshrc_file.read()

    p = re.compile("^ZSH_THEME_RANDOM_IGNORED=\(\s*((?:\w+\s*)+)\)$", re.MULTILINE)
    m = p.search(all)
    if m:
        ignored_theme_names = [x.strip() for x in m.group(1).split(" ")]

    ignored_theme_names.append(new_ignored_theme_name)
    new_line = f"ZSH_THEME_RANDOM_IGNORED=({' '.join(ignored_theme_names)})"

    if m:
        new_all = p.sub(new_line, all)
    else:
        new_all = f"{all}\n{new_line}"

    with open(zshrc_path, "w") as zshrc_file:
        zshrc_file.write(new_all)


def main():
    assert len(sys.argv) == 2, "Usage: main.py <theme_name>"
    random_theme = sys.argv[1]

    add_ignored_theme_to_zshrc(random_theme)


if __name__ == "__main__":
    main()
