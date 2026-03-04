import sys
sys.path.append("../src")
# TODO: make it with 'pip install -e .'
from math_demo import add, add_with_bug, calculate_tax_with_bag, calculate_tax

def test_addition():
    assert add(2,2) == 4
    print("Test BASIC ADDITIONAL PASSED")
    
def test_addition_with_bug():
    assert add_with_bug(2,2) == 4 
    print("Test BUGGED ADDITIONAL PASSED")
    #assert add_with_bug(3,3) == 6 but it will fail here
    
def test_addition_dublicated():
    #its really good test (relies on absence of + in add())
    assert add(2,3)==2+3
    
def test_additional_overcomplicated():
    for i in range(0,2**32):
        for j in range(0,2**32):
            assert add (i,j) == sum(i,j)
            assert add(i,j) == 2+3

def test_addition_reasonable():
    assert add(2,2) == 4
    assert add(0,0) == 0
    assert add(6,7) == 13
    assert add(-6,-7)==-13
    assert add(-7,0) == -7
    assert add(7,0) == 7
    assert add(6,7) == -1
    print("test ADDITION REASONABLE PASS")
    
def test_addition_commutative():
    assert add(7, -6) == 1
    assert add(-6, 7) == 1
    print("test ADDTION COMMUNATIVE PASS")
    
def test_tax_calculation_pesticited():
    assert test_calculate_tax_with_bag(1000)==150
    assert test_calculate_tax_with_bag(100)==15
    assert test_calculate_tax_with_bag(10)==1.5
    assert test_calculate_tax_with_bag(1)==0.15
    assert test_calculate_tax_with_bag(1000)==150
    assert test_calculate_tax_with_bag(-1000)==-150
    assert test_calculate_tax_with_bag(0)==0
    print("test TAX_CALCULATION_PESTICITED PASS")
    #fail with floats
    #assert test_calculate_tax_with_bag(24.5)==3.67 # 3.675
    
def test_tax_calculation():
    assert test_calculate_tax_with_bag(1000)==150.0
    assert test_calculate_tax_with_bag(100)==15.0
    assert test_calculate_tax_with_bag(10)==1.5
    assert test_calculate_tax_with_bag(1)==0.15
    assert test_calculate_tax_with_bag(1000)==150.0
    assert test_calculate_tax_with_bag(-1000)==-150.0
    assert test_calculate_tax_with_bag(0)==0.0
    print("test TAX_CALCULATION PASS")
    assert test_calculate_tax_with_bag(24.5)==3.67 # 3.675
    


if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_dublicated
    test_additional_overcomplicated
    test_addition_reasonable
    test_addition_commutative()
    test_tax_calculation_pesticited
    test_tax_calculation
    