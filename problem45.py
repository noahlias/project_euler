def is_pentagonal(n: int) -> bool:
    """Pentagonal

    Returns True if n is pentagonal, False otherwise.
    >>> is_pentagonal(330)
    True
    >>> is_pentagonal(7683)
    False
    >>> is_pentagonal(2380)
    True
    """
    root = (1 + 24 * n) ** 0.5
    return ((1 + root) / 6) % 1 == 0


def solution():
    """Solution

    Triangle, pentagonal, and hexagonal numbers
    """
    n = 144
    num = n * (2 * n - 1)
    while not is_pentagonal(num):
        n += 1
        num = n * (2 * n - 1)
    return num


if __name__ == "__main__":
    print(solution())
