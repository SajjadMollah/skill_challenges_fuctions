from lib.age_checker import *


def test_age_allowed_over_16():
    result = AgeAllowed("2003-04-14")
    assert result == "Access Granted"

def test_age_allowed_under_16():
    result = AgeAllowed("2010-04-14")
    assert result == "Access Denied. You need to be 16 and you are 14."

def test_age_allowed_incorrect_format():
    result = AgeAllowed("2003-4-1")
    assert result == "Invalid Date"
    