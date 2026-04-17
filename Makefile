VENV = .venv
PY   = $(VENV)/bin/python
PIP  = $(VENV)/bin/pip

venv:
	python3 -m venv $(VENV)

install: venv
	$(PIP) install -r requirements.txt

check-requirements:
	$(PY) scripts/check_requirements.py src/ requirements.txt