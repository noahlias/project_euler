def solution(n: int = 1000) -> int:
    """Get the first one thousand expansions

    Return how many fraction with more digits then denominator
    """
    ans = 0
    for i in range(1, n + 1):
        if len(str(fraction(i)[0])) > len(str(fraction(i)[1])):
            ans += 1
    return ans


def fraction(n):
    """Get the Square root convergents

    The Formula:
    f(1) = (1,2)
    f(2) = 1/ 2 + 1
    f(n) = 1/ (2+f(n-1) - 1) +1 this is the formula
        = (2+ f(n-1))/(1+ f(n-1))
    f(n-1)  = numerator / denominator
    f(n) = 2*denominator + numerator / (numerator + denominator)
    >>> fraction(1)
    >>> (3,2)
    >>> fraction(4)
    >>> (41,29)
    >>> fraction(8)
    >>> (1393,985)
    """
    # if n == 1:
    #     return (3, 2)
    # return (
    #     fraction(n - 1)[1] * 2 + fraction(n - 1)[0],
    #     fraction(n - 1)[0] + fraction(n - 1)[1],
    # )
    if n == 1:
        return 3, 2
    p, q = 3, 2
    for _ in range(2, n + 1):
        p, q = 2 * q + p, p + q
    return p, q


if __name__ == "__main__":
    print(fraction(7))
    print(solution())
