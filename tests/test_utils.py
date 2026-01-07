"""
utils.py 테스트 모듈

이 테스트들이 모두 통과하도록 src/utils.py를 구현하세요.
"""

import pytest
from src.utils import validate_numbers, round_result, format_output


class TestValidateNumbers:
    """validate_numbers 함수 테스트"""

    def test_all_integers(self):
        """모두 정수"""
        assert validate_numbers([1, 2, 3]) is True

    def test_all_floats(self):
        """모두 실수"""
        assert validate_numbers([1.5, 2.5, 3.5]) is True

    def test_mixed_numbers(self):
        """정수와 실수 혼합"""
        assert validate_numbers([1, 2.5, 3]) is True

    def test_with_string(self):
        """문자열 포함"""
        assert validate_numbers([1, "a", 3]) is False

    def test_with_none(self):
        """None 포함"""
        assert validate_numbers([1, None, 3]) is False

    def test_empty_list(self):
        """빈 리스트"""
        assert validate_numbers([]) is True

    def test_with_list(self):
        """리스트 포함"""
        assert validate_numbers([1, [2, 3], 4]) is False


class TestRoundResult:
    """round_result 함수 테스트"""

    def test_default_decimals(self):
        """기본 소수점 2자리"""
        assert round_result(3.14159) == 3.14

    def test_three_decimals(self):
        """소수점 3자리"""
        assert round_result(3.14159, 3) == 3.142

    def test_zero_decimals(self):
        """소수점 0자리 (정수)"""
        assert round_result(3.6, 0) == 4.0

    def test_one_decimal(self):
        """소수점 1자리"""
        assert round_result(3.14159, 1) == 3.1

    def test_no_rounding_needed(self):
        """반올림 필요 없음"""
        assert round_result(3.14, 2) == 3.14


class TestFormatOutput:
    """format_output 함수 테스트"""

    def test_basic_format(self):
        """기본 포맷"""
        assert format_output("평균", 3.14159) == "평균: 3.14"

    def test_zero_decimals(self):
        """소수점 없음"""
        assert format_output("합계", 100.0, 0) == "합계: 100"

    def test_three_decimals(self):
        """소수점 3자리"""
        assert format_output("결과", 3.14159, 3) == "결과: 3.142"

    def test_korean_name(self):
        """한글 이름"""
        assert format_output("중앙값", 5.0) == "중앙값: 5.0"

    def test_english_name(self):
        """영어 이름"""
        assert format_output("Mean", 3.5) == "Mean: 3.5"
