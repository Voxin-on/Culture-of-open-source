# vectors-calc

Библиотека для базовых операций над векторами: сложение и скалярное произведение.

Репозиторий: https://github.com/Voxin-on/Culture-of-open-source

---

## Описание

Проект реализует две функции:

- `vector_add(v1, v2)` — поэлементное сложение двух векторов одинаковой длины
- `scalar_product(v1, v2)` — скалярное произведение двух векторов одинаковой длины

Обе функции выбрасывают `ValueError` если длины векторов не совпадают.

---

## Установка

### С test.pypi

```bash
pip install --index-url https://test.pypi.org/simple/ vectors-calc
```

### Из исходников

```bash
git clone https://github.com/Voxin-on/Culture-of-open-source
cd Culture-of-open-source
git checkout pypi-release-branch
pip install -e .
```

---

## Использование

```python
from vectors import vector_add, scalar_product

vector_add([1, 2, 3], [4, 5, 6])      # [5, 7, 9]
scalar_product([1, 2, 3], [4, 5, 6])  # 32
```

---

## Разработка

### Требования

- Python 3.10+
- pytest
- flake8
- mypy
- build
- twine

```bash
pip install -r requirements.txt
```

### Последовательность действий

1. Установить зависимости
```bash
make install
```

2. Проверить стиль кода
```bash
make lint
```

3. Проверить типы
```bash
make typecheck
```

4. Запустить тесты
```bash
make test
```

5. Собрать пакет
```bash
make build
```

6. Всё сразу
```bash
make all
```

---

## Тесты

```bash
make test
```

Покрывают: базовые случаи, нули, отрицательные числа, вещественные числа, ортогональные векторы, ошибку при разных длинах.