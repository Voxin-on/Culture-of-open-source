def vector_add(v1: list, v2: list) -> list:
    """Складывает два вектора одинаковой длины."""
    if len(v1) != len(v2):
        raise ValueError("Векторы должны быть одинаковой длины")
    return [x + y for x, y in zip(v1, v2)]

def scalar_product(v1: list, v2: list) -> float:
    """Вычисляет скалярное произведение векторов."""
    if len(v1) != len(v2):
        raise ValueError("Векторы должны быть одинаковой длины")
    return sum(x * y for x, y in zip(v1, v2))