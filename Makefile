VENV = $(CURDIR)/.venv/bin

.PHONY: none

install_requirements:
	@$(VENV)/python -m pip install -r requirements/main.txt -r requirements/dev.txt

compile_requirements:
	@$(VENV)/pip-compile --allow-unsafe --generate-hashes requirements/main.in > requirements/main.txt
	@$(VENV)/pip-compile --allow-unsafe --generate-hashes requirements/dev.in > requirements/dev.txt

flake8:
	@$(VENV)/python -m flake8 $(CURDIR)
