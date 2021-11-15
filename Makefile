cov-pytest:
	python -m coverage run --source=omz_theme_ignore -m pytest --disable-warnings -vv -x
	python -m coverage report -m