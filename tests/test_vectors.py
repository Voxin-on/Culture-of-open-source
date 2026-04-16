import pytest
from vectors import vector_add, scalar_product


# vector_add

def test_vector_add_basic():
    assert vector_add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def test_vector_add_zeros():
    assert vector_add([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_vector_add_negative():
    assert vector_add([-1, -2], [1, 2]) == [0, 0]

def test_vector_add_floats():
    assert vector_add([1.5, 2.5], [0.5, 0.5]) == [2.0, 3.0]

def test_vector_add_different_lengths():
    with pytest.raises(ValueError):
        vector_add([1, 2], [1, 2, 3])

# scalar_product

def test_scalar_product_basic():
    assert scalar_product([1, 2, 3], [4, 5, 6]) == 32

def test_scalar_product_zeros():
    assert scalar_product([0, 0, 0], [1, 2, 3]) == 0

def test_scalar_product_negative():
    assert scalar_product([-1, -2], [1, 2]) == -5

def test_scalar_product_orthogonal():
    assert scalar_product([1, 0], [0, 1]) == 0

def test_scalar_product_different_lengths():
    with pytest.raises(ValueError):
        scalar_product([1, 2], [1, 2, 3])