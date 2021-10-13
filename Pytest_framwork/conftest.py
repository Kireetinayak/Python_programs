import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("i will execute at last")