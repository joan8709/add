"""
calculator.py 테스트 모듈

이 테스트들이 모두 통과하도록 src/calculator.py를 구현하세요.
"""

import pytest
from src.calculator import add, subtract, multiply, divide


class TestAdd:
    """add 함수 테스트"""

    def test_positive_numbers(self):
        """양수 덧셈"""
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        """음수 덧셈"""
        assert add(-1, -1) == -2

    def test_mixed_numbers(self):
        """양수와 음수 덧셈"""
        assert add(-1, 1) == 0

    def test_with_zero(self):
        """0과의 덧셈"""
        assert add(5, 0) == 5
        assert add(0, 5) == 5

    def test_floats(self):
        """소수점 덧셈"""
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    """subtract 함수 테스트"""

    def test_positive_result(self):
        """결과가 양수"""
        assert subtract(5, 3) == 2

    def test_negative_result(self):
        """결과가 음수"""
        assert subtract(3, 5) == -2

    def test_same_numbers(self):
        """같은 수 빼기"""
        assert subtract(5, 5) == 0

    def test_with_zero(self):
        """0 빼기"""
        assert subtract(5, 0) == 5


class TestMultiply:
    """multiply 함수 테스트"""

    def test_positive_numbers(self):
        """양수 곱셈"""
        assert multiply(3, 4) == 12

    def test_negative_numbers(self):
        """음수 곱셈"""
        assert multiply(-2, -3) == 6

    def test_mixed_sign(self):
        """부호가 다른 곱셈"""
        assert multiply(-2, 3) == -6

    def test_with_zero(self):
        """0 곱셈"""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0

    def test_with_one(self):
        """1 곱셈"""
        assert multiply(5, 1) == 5


class TestDivide:
    """divide 함수 테스트"""

    def test_exact_division(self):
        """나누어 떨어지는 나눗셈"""
        assert divide(10, 2) == 5.0

    def test_non_exact_division(self):
        """나누어 떨어지지 않는 나눗셈"""
        assert divide(7, 2) == 3.5

    def test_negative_result(self):
        """결과가 음수"""
        assert divide(-10, 2) == -5.0

    def test_divide_by_zero(self):
        """0으로 나누기 - ZeroDivisionError 발생해야 함"""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    def test_zero_divided(self):
        """0을 나누기"""
        assert divide(0, 5) == 0.0
