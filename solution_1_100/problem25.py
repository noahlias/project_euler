def fib(n: int):
    """_summary_

    Args:
        n (int): _description_

    Returns:
        _type_: _description_
    """
    if n <= 2:
        return 1
    p, q = 1, 1
    for i in range(3, n + 1):
        p, q = q, p + q
    return q


def solution(digit: int = 3) -> int:
    """_summary_

    Args:
        digit (int, optional): _description_. Defaults to 3.

    Returns:
        int: _description_
    """
    i = 1
    while True:
        if len(str(fib(i))) == digit:
            break
        i += 1
    return i, fib(i)


if __name__ == "__main__":
    print(solution())
    print(solution(1000))
