#Import pytest and task7.py
import pytest
from src.task7 import dot_prod

#Check to see if dot product works
def test_dot_product():
    assert dot_prod([1, 2, 3], [4, 5, 6]) == 32

#With zero matric dot product we get zero
def test_dot_product_zeros():
    assert dot_prod([1, 2, 3], [0, 0, 0]) == 0

