"""
statistics.py 테스트 모듈

이 테스트들이 모두 통과하도록 src/statistics.py를 구현하세요.
"""

import pytest
from src.statistics import mean, median, mode, variance


class TestMean:
    """mean 함수 테스트"""

    def test_simple_mean(self):
        """간단한 평균"""
        assert mean([1, 2, 3, 4, 5]) == 3.0

    def test_two_numbers(self):
        """두 숫자의 평균"""
        assert mean([10, 20]) == 15.0

    def test_single_number(self):
        """하나의 숫자"""
        assert mean([5]) == 5.0

    def test_with_floats(self):
        """소수점 포함"""
        assert mean([1.5, 2.5, 3.0]) == pytest.approx(2.333, rel=0.01)

    def test_empty_list(self):
        """빈 리스트 - ValueError 발생해야 함"""
        with pytest.raises(ValueError):
            mean([])


class TestMedian:
    """median 함수 테스트"""

    def test_odd_count(self):
        """홀수 개의 숫자"""
        assert median([1, 3, 5]) == 3

    def test_even_count(self):
        """짝수 개의 숫자"""
        assert median([1, 2, 3, 4]) == 2.5

    def test_unsorted_list(self):
        """정렬되지 않은 리스트"""
        assert median([5, 1, 3]) == 3

    def test_single_number(self):
        """하나의 숫자"""
        assert median([7]) == 7

    def test_two_numbers(self):
        """두 숫자"""
        assert median([1, 3]) == 2.0

    def test_empty_list(self):
        """빈 리스트 - ValueError 발생해야 함"""
        with pytest.raises(ValueError):
            median([])


class TestMode:
    """mode 함수 테스트"""

    def test_clear_mode(self):
        """명확한 최빈값"""
        assert mode([1, 2, 2, 3, 3, 3]) == 3

    def test_tie_first_wins(self):
        """동률일 때 먼저 나온 값"""
        assert mode([1, 1, 2, 2]) == 1

    def test_all_same(self):
        """모두 같은 값"""
        assert mode([5, 5, 5]) == 5

    def test_single_number(self):
        """하나의 숫자"""
        assert mode([7]) == 7

    def test_empty_list(self):
        """빈 리스트 - ValueError 발생해야 함"""
        with pytest.raises(ValueError):
            mode([])


class TestVariance:
    """variance 함수 테스트"""

    def test_simple_variance(self):
        """간단한 분산"""
        # [1,2,3,4,5]의 평균 = 3
        # 분산 = ((1-3)^2 + (2-3)^2 + (3-3)^2 + (4-3)^2 + (5-3)^2) / 5
        #      = (4 + 1 + 0 + 1 + 4) / 5 = 2.0
        assert variance([1, 2, 3, 4, 5]) == 2.0

    def test_zero_variance(self):
        """분산이 0 (모든 값이 같음)"""
        assert variance([5, 5, 5, 5]) == 0.0

    def test_single_number(self):
        """하나의 숫자"""
        assert variance([5]) == 0.0

    def test_empty_list(self):
        """빈 리스트 - ValueError 발생해야 함"""
        with pytest.raises(ValueError):
            variance([])
