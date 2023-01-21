import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(3, 8) == 24

    def test_division_success(self):
        assert self.calc.division(12, 3) == 4

    def test_subtraction_success(self):
        assert self.calc.subtraction(10, 7) == 3

    def test_adding_success(self):
        assert self.calc.adding(10, 5) == 15

    def teardown(self):
        print("Выполнение метода Teardown")
