# Import task1 and functions
from src.task1 import main

#test HelloWorld Function with capsys
def test_HelloWrld(capsys):
    #Call main
    main()
    #Capture tje output
    capture = capsys.readouterr()
    #Check to see if its matches what we expect
    assert capture.out == "Hello, World!\n"