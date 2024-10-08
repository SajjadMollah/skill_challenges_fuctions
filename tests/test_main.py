from lib.main import *

def test_make_snippet():
    text = Diary()
    result = text.make_snippet("Hello my name is kay and im from Uk")
    assert result == "Hello my name is kay..."

def test_count_words():
    text = Diary()
    result = text.count_words("Hello my name is kay and im from Uk")
    assert result == 9