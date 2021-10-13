import  pytest
from selenium import webdriver
@pytest.mark.smoketest
def test_m1():
    a=3
    b=4
    assert a+1==b, "test is failed"
    assert b==a, "Test is failed because a is not equal to b"

def test_m2():
    name="selenium"
    assert name.upper()=="SELENIUM", "word is matched"

def test_m3():
    assert True
@pytest.mark.smoketest
def test_m4():
    assert False