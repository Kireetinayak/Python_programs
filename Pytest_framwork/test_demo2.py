import pytest

#@pytest.mark.skip
def test_program11():
    msg="hello"
    assert msg == "Hi","Test failed becase string doesnot match"

@pytest.mark.smoke
def test_credit_card_program12():
    a=4
    b=3
    assert a+2==6,"Addition does not match"
