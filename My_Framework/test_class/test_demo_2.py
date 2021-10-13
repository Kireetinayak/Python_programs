import pytest

def test_m11():
    name1="kireeti"
    assert name1.lower()=="kireeti", "Text matched"
    assert name1.upper()=="KIREETi", "Test not matched"

@pytest.mark.smoketest
def test_m12():
    assert  True

