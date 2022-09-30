from math import gcd, sqrt


def genTriples(k):
    """_summary_

    Args:
        k (_type_): _description_

    Returns:
        _type_: _description_

    Yields:
        _type_: _description_
    """
    # primitive pythagorean triangles a,b,c where a<b<c<k
    n, m = 1, 2
    while m * m + 1 < k:
        if n >= m:
            n, m = m % 2, m + 1
        c = m * m + n * n
        if c >= k:
            n = m
            continue
        if gcd(n, m) == 1:
            yield m * m - n * n, 2 * m * n, c
        n += 2


def solve(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    a, b, c, total = 3, 4, 5, 0
    while 2 * (a + c) <= n:
        total += 2 * (a + c)
        a, b, c = -2 * a + b + 2 * c, -a + 2 * b + 2 * c, -2 * a + 2 * b + 3 * c
    return total


def primitive_pythagorean_triangles():
    """Primitive_pythagorean_triangles

    Return sum
    """
    N = 1000000000
    result = 0
    ans = []
    for a, b, c in genTriples(N // 3 + 2):
        if abs(2 * a - c) == 1:
            result += 2 * a + 2 * c
            ans.append((c, c, 2 * a))
        if abs(2 * b - c) == 1:
            result += 2 * b + 2 * c
            ans.append((c, c, 2 * b))
    return result, ans


def almostEqui(maxPerimeter):
    """_summary_

    Args:
        maxPerimeter (_type_): _description_

    Yields:
        _type_: _description_
    """
    h = 1
    for c in range(2, maxPerimeter // 3 + 2, 2):
        cc4 = c * c // 4
        for a in (c - 1, c + 1):
            hh = a * a - cc4
            while h * h < hh:
                h += 1
            if h * h == hh and 2 * a + c <= maxPerimeter:
                yield a, a, c
        h -= 1


def is_square(n: int) -> bool:
    """Square

    Args:
        n (int): _description_

    Returns:
        bool: _description_
    """
    return n == int(sqrt(n)) ** 2


def solution(n: int) -> int:
    """Return the the sum of the perimeters

    Args:
        n (int): _description_

    Returns:
        int: _description_
    """
    total = 0
    ans = []
    for i in range(1, n + 1):
        if (
            i % 2 != 0
            and (
                is_square(i**2 - (i + 1) ** 2 / 4)
                or is_square(i**2 - (i - 1) ** 2 / 4)
            )
            and i > 1
        ):
            total += 3 * i + 1
            ans.append((i, i, i + 1))
    return total, ans


if __name__ == "__main__":
    # print(solution(10**9 // 3 + 1))
    # print(primitive_pythagorean_triangles())
    print(solve(1_000_000_000))
    # print(sum(a + b + c for a, b, c in almostEqui(1000000000)))
