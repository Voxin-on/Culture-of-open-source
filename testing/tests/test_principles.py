import sys
sys.path.append("../src")
# TODO: make it with 'pip install -e .'
from math_demo import add, add_with_bug

def test_addition():
    assert add(2,2) == 4
    print("Test BASIC ADDITIONAL PASSED")
    
def test_addition_with_bug():
    assert add_with_bug(2,2) == 4 
    print("Test BUGGED ADDITIONAL PASSED")
    #assert add_with_bug(3,3) == 6 but it will fail here
    
if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    