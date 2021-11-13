import os
import sys

# Extend section ZSH_THEME_RANDOM_IGNORED in the .zshrc file with theme name
def add_ignored_themes_to_zshrc(ignored_theme_names):
    # remove duplicates from ignored_theme_names list
    ignored_theme_names = sorted(list(set(ignored_theme_names)))
    in_ignored_themes = False
    zshrc_path = os.path.expanduser("~/.zshrc_bak")
    with open(zshrc_path, "r") as zshrc_file:
        zshrc_lines = zshrc_file.readlines()

    new_line = "ZSH_THEME_RANDOM_IGNORED=(" + " ".join(ignored_theme_names) + ")\n"
    zshrc_new_lines = []

    for line in zshrc_lines:
        if "ZSH_THEME_RANDOM_IGNORED" in line:
            if not ")" in line:
                in_ignored_themes = True
            zshrc_new_lines.append(new_line)
        elif in_ignored_themes:
            if ")" in line:
                in_ignored_themes = False
        else:
            zshrc_new_lines.append(line)
    with open(zshrc_path, "w") as zshrc_file:
        zshrc_file.write("".join(zshrc_new_lines))


# Get items from ZSH_THEME_RANDOM_IGNORED section from the .zshrc file
def get_ignored_themes_from_zshrc():
    zshrc_path = os.path.expanduser("~/.zshrc_bak")
    ignored_themes = []
    in_ignored_themes = False
    with open(zshrc_path, "r") as zshrc_file:
        for line in zshrc_file:
            if "ZSH_THEME_RANDOM_IGNORED" in line:
                if ")" in line:
                    return line.split("=")[1].split("(")[1].split(")")[0].split(" ")
                else:
                    in_ignored_themes = True
            elif in_ignored_themes:
                if ")" in line:
                    in_ignored_themes = False
                else:
                    ignored_themes.append(line.strip())
    return ignored_themes


def main():
    assert len(sys.argv) == 2, "Usage: main.py <theme_name>"
    random_theme = sys.argv[1]

    current = get_ignored_themes_from_zshrc()
    current.append(random_theme)
    add_ignored_themes_to_zshrc(current)


if __name__ == "__main__":
    main()
