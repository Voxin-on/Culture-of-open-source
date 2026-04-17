# Make-автоматизация Python-проекта

## Описание

Проект демонстрирует автоматизацию типичных задач разработки через Makefile.
Все инструменты запускаются через `.venv/bin/` — это гарантирует использование
проектного окружения, а не системного.

## Команды

| Команда | Действие |
| `make venv` | Создаёт `.venv/` |
| `make install` | Устанавливает зависимости в `.venv/` |
| `make typecheck` | Проверяет типы через mypy |
| `make lint` | Проверяет стиль через flake8 |
| `make format` | Форматирует код через black |
| `make check-requirements` | Сравнивает импорты с requirements.txt |
| `make check` | Запускает typecheck + check-requirements |

## Быстрый старт

```bash
make install
make check
```