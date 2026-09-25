#Import pytets for paramatized test
import pytest
from src.task2 import int_add,float_prod,is_string,comp_func_

#Pass in these test parameters
@pytest.mark.parametrize("n1,n2,expected",[
    (2,3,5),
    (10,5,15),
    (-3,5,2)
])
#Run add
def test_int_add(n1,n2,expected):
    assert int_add(n1,n2) == expected

#Pass in test params
@pytest.mark.parametrize("f1,f2,product",[
    (2.5,4.0,10.0),
    (1.5,2.0,3.0),
    (5.5,2.0,11.0)
])
#Run float product
def test_float_prod(f1,f2,product):
    assert float_prod(f1,f2) == product

#Run to see if is_string returns a string
def test_is_string():
    assert is_string() == "This is a string"

#Pass in params
@pytest.mark.parametrize("c1,c2,comparison",[
    (2,2,True),
    (3,2,False)
])
#Check Bools
def test_bool_func(c1,c2,comparison):
    assert comp_func_(c1,c2) == comparison