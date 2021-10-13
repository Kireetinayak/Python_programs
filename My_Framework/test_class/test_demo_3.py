import  pytest

@pytest.mark.smoketest
def test_m21():
    print("kireeti nayak")
    assert 4==4, "Value is equal"

def test_m22():
    k="king"
    assert k.upper()=="KING", "Value is equals"
