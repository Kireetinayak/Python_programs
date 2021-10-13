# Pytest file should start with test_
# Pytes methos name should start with test_

import pytest

@pytest.mark.usefixtures("setup")
class Testexample:
    def test_program1(self):
        print("program1")

    @pytest.mark.smoke
    def test_credit_card_number_program2(self):
        print("program2")

    def test_program3(self):
        print("program3")