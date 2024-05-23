from Calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 2024
        b = 2005
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 19
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 12
        b = 3
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 36
        assert result == expected

    def test_divide(self):
        # arrange
        a = 12
        b = 3
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 4
        assert result == expected

    def test_divide_byZero(self):
        # arrange
        a = 12
        b = 0
        cal = Calculator()

        #act and insert
        with pytest.raises(ZeroDivisionError):
            cal.divide(12,0)
            
