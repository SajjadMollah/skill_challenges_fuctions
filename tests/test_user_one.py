from lib.user_one import *



def test_read_time():
    result = read_time("Nature is not just")
    assert result == 0.02


def test_check_grammar():
    result = check_grammar("Hello my name is Sajjad.")
    assert result == "The grammar is correct"