# Import pytest and function
import pytest
from src.task6 import count_Words

#Set file name as param
@pytest.mark.parametrize("filename", [
    "task6_read_me.txt"
])
#Run and see if it macthes 127 the actual word count
def test_count_words(filename):
    assert count_Words(filename) == 127
