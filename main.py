import os
import sys
import re


# Extend section ZSH_THEME_RANDOM_IGNORED in the .zshrc file with theme names
def add_ignored_themes_to_zshrc(ignored_theme_names):
    # remove duplicates from ignored_theme_names list
    ignored_theme_names = sorted(list(set(ignored_theme_names)))
    zshrc_path = os.path.expanduser("~/.zshrc_bak")
    with open(zshrc_path, "r") as zshrc_file:
        all = zshrc_file.read()

    p = re.compile("^ZSH_THEME_RANDOM_IGNORED=\(\s*((?:\w+\s*)+)\)$", re.MULTILINE)
    new_line = "ZSH_THEME_RANDOM_IGNORED=(" + " ".join(ignored_theme_names) + ")"
    new_all = p.sub(new_line, all)

    with open(zshrc_path, "w") as zshrc_file:
        zshrc_file.write(new_all)


def get_ignored_themes_from_zshrc():
    zshrc_path = os.path.expanduser("~/.zshrc_bak")
    ignored_themes = []
    with open(zshrc_path, "r") as zshrc_file:
        all = zshrc_file.read()
    p = re.compile("^ZSH_THEME_RANDOM_IGNORED=\(\s*((?:\w+\s*)+)\)$", re.MULTILINE)
    m = p.search(all)
    if m:
        ignored_themes = m.group(1).split(" ")
    return [x.strip() for x in ignored_themes]


def main():
    assert len(sys.argv) == 2, "Usage: main.py <theme_name>"
    random_theme = sys.argv[1]

    current = get_ignored_themes_from_zshrc()
    current.append(random_theme)
    add_ignored_themes_to_zshrc(current)


if __name__ == "__main__":
    main()
