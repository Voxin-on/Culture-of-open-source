.PHONY: create-structure

create-structure:
	mkdir -p src tests docs
	touch src/.gitkeep tests/.gitkeep
	touch docs/DOMAIN.md README.md .gitignore
	touch setup.py requirements.txt

reqs:
	pipreqs . --force --ignore venv

run:
	poetry install
	poetry run uvicorn app.main:app --host 127.0.0.1 --port 8002