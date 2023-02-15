
from random import randint
import socket1

def test_calculateAbsolute_printsABS_lessThan21(capfd, monkeypatch):
    in_num = randint(-100, 21)
    input = [in_num]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    socket1.assignment_12_1()

    out, err = capfd.readouterr()
       
    assert "Status:" in out
    assert "HTTP/1.1 200 OK" in out
    assert "Headers:" in out
    assert "Content-Length: 467" in out
    assert "Content-Type: text/plain" in out
    assert "Data:" in out
    assert "Why should you learn to write programs?" in out
    assert "Writing programs (or programming) is a very creative " in out
    assert "and rewarding activity.  You can write programs for" in out
    assert "many reasons, ranging from making your living to solving" in out
    assert "a difficult data analysis problem to having fun to helping" in out
    assert "someone else solve a problem.  This book assumes that " in out
    assert "everyone needs to know how to program, and that once " in out
    assert "you know how to program you will figure out what you want " in out
    assert "to do with your newfound skills. " in out
