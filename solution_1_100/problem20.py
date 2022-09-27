from math import factorial


def solution(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    num = factorial(n)
    r = 0
    while num != 0:
        r = r + num % 10
        num = num // 10
    return r


if __name__ == "__main__":
    print(solution(10))
    print(solution(100))
