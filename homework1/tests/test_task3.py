#Import pytest
import pytest
from src.task3 import checkNumberSign,first_10_prime_nums,one_too_onehundred

#Parameters we pass
@pytest.mark.parametrize("num,expectedsign",[
    (5, "5 is positive\n"),
    (-5, "-5 is negative\n"),
    (0, "0 is 0\n")
])
#Then check if output macthes
def test_checkNumberSign(num,expectedsign,capsys):
    #Call function and check if the outputs match
    checkNumberSign(num)
    #Use .out to get string output, this was giving issue if I did not have .out
    outcome = capsys.readouterr().out
    assert outcome == expectedsign

#Check the first 10 prime nums call and comp output
def test_firest_10_prime_nums(capsys):
    first_10_prime_nums()
    primeL = capsys.readouterr().out
    assert primeL == "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"

#Call one_too_onehundred and see if its is 5050
def test_one_too_onehundred():
    assert one_too_onehundred() == 5050
