import io
from random import randint
from unittest.mock import Mock
import oddAbsolute

def test_calculateAbsolute_printsABS_lessThan21(capfd, monkeypatch):
    in_num = randint(-100, 21)
    input = [in_num]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    socket1.getWebData()

    out, err = capfd.readouterr()
    expected = "Why should you learn to write programs?\n\n" 
                "Writing programs (or programming) is a very creative \n"
                "and rewarding activity.  You can write programs for \n"
                "many reasons, ranging from making your living to solving\n"
                "a difficult data analysis problem to having fun to helping\n"
                "someone else solve a problem.  This book assumes that \n"
                "everyone needs to know how to program, and that once \n"
                "you know how to program you will figure out what you want \n"
                "to do with your newfound skills.  "
    assert out == expected
