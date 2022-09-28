from functools import lru_cache


def solution(n: int, digit: int = 2) -> int:
    """Return the first digit consecutive integers

    Args:
        n (int): _description_
        digit (int, optional): _description_. Defaults to 2.

    Returns:
        int: _description_
    """
    for i in range(1, n + 1):
        if all(divisor(i + j) == digit for j in range(digit)):
            return i


@lru_cache(maxsize=10)
def divisor(n: int):
    """Get all the prime factor

    Args:
        num (_type_): _description_

    Returns:
        _type_: _description_
    """
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


def get_max_divisor_count():
    """Max divisor count

    [51051,570570,690690,746130,870870,903210,930930]
    Returns:
        _type_: _description_
    """
    count = 0
    for i in range(2, 1_000_000 + 1):
        if len(divisor(i)) == 7:
            print(i)
        count = max(count, len(divisor(i)))
    return count


if __name__ == "__main__":
    print(divisor(881790))
    print(get_max_divisor_count())
    # print(solution(10000, 3))
    # print(solution(1000000, 4))
