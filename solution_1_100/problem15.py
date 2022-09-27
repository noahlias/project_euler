from math import factorial


def solution(n: int) -> int:
    """Solve problem 15

    Starting in the top left corner of a 2×2 grid
    and only being able to move to the right and down
    , there are exactly 6 routes to the bottom right corner.
    >>> solution(2)
    >>> 6
    >>> solution(20)
    >>> 137846528820
    """
    dp = [[1] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


def solution_math(n: int) -> int:
    """Use factorial solution

    result = factorial(2*n)//factorial(n)**2
    >>> solution_math(20)
    >>> 137846528820
    """
    return factorial(2 * n) // (factorial(n) ** 2)


if __name__ == "__main__":
    print(solution(2))
    print(solution(20))
    print(solution_math(20))
