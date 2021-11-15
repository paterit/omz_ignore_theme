from omz_theme_ignore.main import build_new_zshrc_content

CONTENT_EMPTY_SECTION_BEFORE = """
ZSH_THEME="random"
ZSH_THEME_RANDOM_IGNORED=()
ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )
"""
CONTENT_EMPTY_SECTION_AFTER = """
ZSH_THEME="random"
ZSH_THEME_RANDOM_IGNORED=(new_theme)
ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )
"""
CONTENT_NO_SECTION_BEFORE = """
ZSH_THEME="random"
ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )
"""
CONTENT_NO_SECTION_AFTER = """
ZSH_THEME="random"
ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

ZSH_THEME_RANDOM_IGNORED=(new_theme)
"""
CONTENT_MULTI_LINE_BEFORE = """
ZSH_THEME="random"
ZSH_THEME_RANDOM_IGNORED=(
  sd27
  sd28
  sd29
)
ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )
"""
CONTENT_MULTI_LINE_AFTER = """
ZSH_THEME="random"
ZSH_THEME_RANDOM_IGNORED=(new_theme sd27 sd28 sd29)
ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )
"""

CONTENT_SINGLE_LINE_BEFORE = """
ZSH_THEME="random"
ZSH_THEME_RANDOM_IGNORED=(sd27 sd28 sd29)
ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )
"""
CONTENT_SINGLE_LINE_AFTER = """
ZSH_THEME="random"
ZSH_THEME_RANDOM_IGNORED=(new_theme sd27 sd28 sd29)
ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )
"""


def test_empty_section():
    assert CONTENT_EMPTY_SECTION_AFTER == build_new_zshrc_content(
        "new_theme", CONTENT_EMPTY_SECTION_BEFORE
    )


def test_multi_line():
    assert CONTENT_MULTI_LINE_AFTER == build_new_zshrc_content(
        "new_theme", CONTENT_MULTI_LINE_BEFORE
    )


def test_duplicates_line():
    assert CONTENT_SINGLE_LINE_BEFORE == build_new_zshrc_content(
        "sd29", CONTENT_SINGLE_LINE_BEFORE
    )


def test_single_line():
    assert CONTENT_SINGLE_LINE_AFTER == build_new_zshrc_content(
        "new_theme", CONTENT_SINGLE_LINE_BEFORE
    )


def test_no_section():
    assert CONTENT_NO_SECTION_AFTER == build_new_zshrc_content(
        "new_theme", CONTENT_NO_SECTION_BEFORE
    )
