import sys
sys.path.append("../src")
#TODO make it with ' pip instal -e .'
from math_demo import add

def test_addition():
    assert add(2,2) == 4
    print("Test: test_addition")
    
if __name__ == "__main__":
    test_addition()