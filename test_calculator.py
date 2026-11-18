import pytest

from calculator import Calculator


class TestCalculator:
    def test_init(self):
        calc = Calculator(2, 17)
        assert (calc.op1, calc.op2) == (2, 17)

    def test_add(self):
        calc = Calculator(-1000, -17)
        assert calc.sum() == -1017

    def test_subtract(self):
        calc = Calculator(2, 17)
        assert calc.subtract() == -15

    def test_multiply(self):
        calc = Calculator(-2, 17)
        assert calc.multiply() == -34

    def test_divide(self):
        for divisor in range(5):
            calc = Calculator(5, divisor+1)
            assert calc.divide() == 5 / (divisor+1)

    def test_divide_by_zero(self):
        calc = Calculator(7, 0)
        with pytest.raises(ZeroDivisionError):
            calc.divide()
