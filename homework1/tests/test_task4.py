#Import functions and pytest
import pytest
from src.task4 import calculate_discount

#Parameters float and int
@pytest.mark.parametrize("price,discount,expected",[
    (100,20,80),
    (50,10,45),
    (100.0,20.0,80.0),
    (50.5,10.0,45.45)
])
#Test for discounts
def test_calculate_discount_normal(price,discount,expected):
    assert calculate_discount(price,discount) == expected

#Parameters that are incorrect
@pytest.mark.parametrize("price,discount",[
    ("100","20"),
    ("100","25")
])
#Check to see if invalid input occurs
def test_calculate_discount_invalid(price,discount):
    #Check if valueError occurs
    with pytest.raises(ValueError):
        calculate_discount(price,discount)