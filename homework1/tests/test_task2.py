from src.task2 import int_add,float_prod,is_string,comp_func_

def test_int_add():
    assert int_add(2,2) == 4


def test_float_prod():
    assert float_prod(3,2) == 6

def test_is_string(capsys):
    is_string()
    capture = capsys.readouterr()
    assert capture.out == "This is a string\n"

def test_bool_func():
    assert comp_func_(2,2) == True
    assert comp_func_(3,2) == False
