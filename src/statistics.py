"""
통계 함수 모듈

담당: 팀원 B
브랜치: feature/statistics
"""

from typing import List

def mean(numbers: List[float]) -> float:
    """숫자 리스트의 평균을 반환합니다.

    Args:
        numbers: 숫자 리스트

    Returns:
        평균값

    Raises:
        ValueError: 빈 리스트일 경우

    Examples:
        >>> mean([1, 2, 3, 4, 5])
        3.0
        >>> mean([10, 20])
        15.0
    """
    if not numbers:
        raise ValueError("빈 리스트에는 평균을 계산할 수 없습니다.")
    return sum(numbers) / len(numbers)


def median(numbers: List[float]) -> float:
    """숫자 리스트의 중앙값을 반환합니다.

    중앙값: 정렬했을 때 가운데 위치한 값
    - 홀수 개: 가운데 값
    - 짝수 개: 가운데 두 값의 평균

    Args:
        numbers: 숫자 리스트

    Returns:
        중앙값

    Raises:
        ValueError: 빈 리스트일 경우

    Examples:
        >>> median([1, 3, 5])
        3
        >>> median([1, 2, 3, 4])
        2.5
    """
    if not numbers:
        raise ValueError("빈 리스트에는 중앙값을 계산할 수 없습니다.")

    nums = sorted(numbers)
    n = len(nums)
    mid = n // 2

    # 홀수 개
    if n % 2 == 1:
        return nums[mid]

    # 짝수 개
    return (nums[mid - 1] + nums[mid]) / 2

def mode(numbers: List[float]) -> float:
    """숫자 리스트의 최빈값을 반환합니다.

    최빈값: 가장 자주 나타나는 값
    동일한 빈도의 값이 여러 개면 가장 먼저 나온 값을 반환

    Args:
        numbers: 숫자 리스트

    Returns:
        최빈값

    Raises:
        ValueError: 빈 리스트일 경우

    Examples:
        >>> mode([1, 2, 2, 3, 3, 3])
        3
        >>> mode([1, 1, 2, 2])
        1
    """
    if not numbers:
        raise ValueError("빈 리스트에는 최빈값을 계산할 수 없습니다.")

    counts = {}
    first_index = {}

    for i, x in enumerate(numbers):
        counts[x] = counts.get(x, 0) + 1
        if x not in first_index:
            first_index[x] = i

    best_value = numbers[0]
    best_count = -1
    best_first = float("inf")

    for x, count in counts.items():
        idx = first_index[x]
        if count > best_count or (count == best_count and idx < best_first):
            best_value = x
            best_count = count
            best_first = idx

    return best_value
    pass

def variance(numbers: List[float]) -> float:
    """숫자 리스트의 분산을 반환합니다.

    분산: 각 값과 평균의 차이의 제곱의 평균

    Args:
        numbers: 숫자 리스트

    Returns:
        분산값

    Raises:
        ValueError: 빈 리스트일 경우

    Examples:
        >>> variance([1, 2, 3, 4, 5])
        2.0
    """
    if not numbers:
        raise ValueError("빈 리스트에는 분산을 계산할 수 없습니다.")

    n = len(numbers)
    if n == 1:
        return 0.0

    m = mean(numbers)
    return sum((x - m) ** 2 for x in numbers) / n