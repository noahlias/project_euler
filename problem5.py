def solution(n=20):
    i = 0
    while 1:
        i += n * (n - 1)
        nfound = 0
        for j in range(2, n):
            if i % j != 0:
                nfound = 1
                break
        if nfound == 0:
            if i == 0:
                i = 1
            return i


def greatest_common_divisor(x: int, y: int) -> int:
    """
    Euclidean Greatest Common Divisor algorithm
    >>> greatest_common_divisor(0, 0)
    0
    >>> greatest_common_divisor(23, 42)
    1
    >>> greatest_common_divisor(15, 33)
    3
    >>> greatest_common_divisor(12345, 67890)
    15
    """

    return x if y == 0 else greatest_common_divisor(y, x % y)


def lcm(x: int, y: int) -> int:
    """
    Least Common Multiple.
    Using the property that lcm(a, b) * greatest_common_divisor(a, b) = a*b
    >>> lcm(3, 15)
    15
    >>> lcm(1, 27)
    27
    >>> lcm(13, 27)
    351
    >>> lcm(64, 48)
    192
    """

    return (x * y) // greatest_common_divisor(x, y)




## 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
## 1 2 3 5 7 11 13 17 19


if __name__ == '__main__':
    print(solution())