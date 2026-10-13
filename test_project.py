import pytest
from project import *

def test_cal_entr():
    assert cal_entr("") == 0
    assert cal_entr("gggg") == 18.8
    assert cal_entr("/0u=ahD=n5LUmB*n") > 100

def test_is_common():
    assert is_common("Qwerty") == True
    assert is_common("/0u=ahD=n5LUmB*n") == False

def test_score():
    assert get_score("qwerty") == 0
    assert get_score("Tarantino2010") == 3
    assert get_score("/0u=ahD=n5LUmB*n") == 5

def test_evaluate():
    assert evaluate_strength(1) == "Weak"
    assert evaluate_strength(3) == "Mid"
    assert evaluate_strength(5) == "Strong"

def test_crack_time():
    assert evaluate_crack_time(0) == "instantly"
    assert evaluate_crack_time(300) == "practically an eternity"
    assert evaluate_crack_time(77.4) == "~316,144 years"

def test_tips():
    assert len(get_tips("Tarantino2010")) == 2
    assert get_tips("/0u=ahD=n5LUmB*n") == []

def test_generate():
    password = generate()
    assert len(password) == 16
    assert get_tips(password) == []
    assert get_score(password) == 5
