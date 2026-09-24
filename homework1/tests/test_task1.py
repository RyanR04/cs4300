# Import HellowWorldFunc 
from src.task1 import main


def test_HelloWrld(capsys):
    main()
    capture = capsys.readouterr()
    assert capture.out == "Hello World!\n"
