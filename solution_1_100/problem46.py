def solution():
    """_summary_

    Returns:
        _type_: _description_
    """
    i = 9
    while i % 2 != 0:
        if not properse(i):
            break
        i += 2
    return i


def properse(n: int) -> bool:
    """Christian Goldbach

    that every odd composite
    number can be written as the
    sum of a prime and twice a square.
    >>> properse(33)
    >>> True
    """
    i = n
    while i > 0:
        square_number = (n - i) // 2
        if is_prime(i) and (n - i) % 2 == 0 and is_square(square_number):
            print(f"Odd composite {n} Prime number {i},Square number {square_number}")
            return True
        i -= 1
    return False


def is_prime(n: int) -> bool:
    """Prime

    Args:
        n (int): _description_

    Returns:
        bool: _description_
    """
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_square(n: int) -> bool:
    """Square

    Args:
        n (int): _description_

    Returns:
        bool: _description_
    """
    i = 1
    if n == 0:
        return True
    while i * i <= n:
        if n / i == i:
            return True
        i += 1
    return False


if __name__ == "__main__":
    # print(properse(33))
    # print(is_square(16))
    # print(is_square(0))
    print(solution())
