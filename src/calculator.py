"""
기본 사칙연산 계산기 모듈

담당: 팀원 A
브랜치: feature/calculator
"""


def add(a: float, b: float) -> float:
    """두 수의 합을 반환합니다.

    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자

    Returns:
        두 수의 합

    Examples:
        >>> add(1, 2)
        3
        >>> add(-1, 1)
        0
    """
    # TODO: 구현하세요
    pass


def subtract(a: float, b: float) -> float:
    """두 수의 차를 반환합니다.

    Args:
        a: 첫 번째 숫자 (피감수)
        b: 두 번째 숫자 (감수)

    Returns:
        a - b의 결과

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(3, 5)
        -2
    """
    # TODO: 구현하세요
    pass


def multiply(a: float, b: float) -> float:
    """두 수의 곱을 반환합니다.

    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자

    Returns:
        두 수의 곱

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(-2, 3)
        -6
    """
    # TODO: 구현하세요
    pass


def divide(a: float, b: float) -> float:
    """두 수의 나눗셈 결과를 반환합니다.

    Args:
        a: 피제수 (나눠지는 수)
        b: 제수 (나누는 수)

    Returns:
        a / b의 결과

    Raises:
        ZeroDivisionError: b가 0일 경우

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    # TODO: 구현하세요
    # 힌트: b가 0이면 ZeroDivisionError를 발생시켜야 합니다
    pass
