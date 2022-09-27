def solution(n=1000):
    """_summary_

    Args:
        n (int, optional): _description_. Defaults to 1000.

    Returns:
        _type_: _description_
    """
    num = 1 << n
    r = 0
    while num != 0:
        r = r + num % 10
        num = num // 10
    return r


if __name__ == "__main__":
    print(solution(10))
    print(solution(15))
    print(solution(1000))
