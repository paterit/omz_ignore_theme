import os
import sys

random_theme = os.getenv("RANDOM_THEME", "None")
random_theme = os.getenv("VTE_VERSION", "None")

# Extend section ZSH_THEME_RANDOM_IGNORED in the .zshrc file with theme name
def add_ignored_themes_to_zshrc(ignored_theme_names):
    # remove duplicates from ignored_theme_names list
    ignored_theme_names = list(dict.fromkeys(ignored_theme_names))

    zshrc_path = os.path.expanduser("~/.zshrc_bak")
    with open(zshrc_path, "r") as zshrc_file:
        zshrc_lines = zshrc_file.readlines()
    with open(zshrc_path, "w") as zshrc_file:
        for line in zshrc_lines:
            print(line)
            if "ZSH_THEME_RANDOM_IGNORED" in line:
                line = line.split("=")[0] + "=(" + " ".join(ignored_theme_names) + ")"
            zshrc_file.write(line)


# Get items from ZSH_THEME_RANDOM_IGNORED section from the .zshrc file
def get_ignored_themes_from_zshrc():
    zshrc_path = os.path.expanduser("~/.zshrc_bak")
    with open(zshrc_path, "r") as zshrc_file:
        for line in zshrc_file:
            if "ZSH_THEME_RANDOM_IGNORED" in line:
                return line.split("=")[1].split("(")[1].split(")")[0].split(" ")


def main():
    assert len(sys.argv) == 2, "Usage: main.py <theme_name>"
    random_theme = sys.argv[1]

    current = get_ignored_themes_from_zshrc()
    current.append(random_theme)
    print(current)
    add_ignored_themes_to_zshrc(current)
    print(get_ignored_themes_from_zshrc())


if __name__ == "__main__":
    main()
