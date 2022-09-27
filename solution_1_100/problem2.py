def solution():
    """_summary_

    Returns:
        _type_: _description_
    """
    n = 33
    ans = 0
    for i in range(1, n):
        if fib(i) % 2 == 0 and fib(i) < 4000000:
            ans += fib(i)
    return ans


def fib(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n <= 2:
        return n
    p, q = 1, 2
    for _ in range(3, n + 1):
        p, q = q, p + q
    return q


if __name__ == "__main__":
    print(fib(33))
    print(solution())
