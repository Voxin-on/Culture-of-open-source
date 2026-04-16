.PHONY: create-structure install reqs lint typecheck test build clean all

# Инициализация структуры

create-structure:
	mkdir -p src tests docs
	touch src/.gitkeep tests/.gitkeep
	touch docs/DOMAIN.md README.md .gitignore
	touch setup.py requirements.txt

# Зависимости

install:
	pip install -r requirements.txt

reqs:
	pipreqs . --force --ignore venv

# Качество кода

lint:
	flake8 src/ tests/

typecheck:
	mypy src/

# Тестирование

test:
	pytest tests/ -v

# Сборка пакета

build:
	python -m build

# Очистка

clean:
	rm -rf dist/ build/ *.egg-info
	rm -rf .mypy_cache .pytest_cache htmlcov .coverage
	rm -rf docs/_build
	find . -type d -name __pycache__ -exec rm -rf {} +

# Запуск всего

all: install lint typecheck test build