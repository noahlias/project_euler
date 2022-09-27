def solution(limit: int = 1_000_000) -> int:
    """Returns an integer, the solution to the problem

    >>> solution(10)
    31
    >>> solution(100)
    3043
    >>> solution(1_000)
    304191
    """
    phi = [i - 1 for i in range(limit + 1)]

    for i in range(2, limit + 1):
        if phi[i] == i - 1:
            for j in range(2 * i, limit + 1, i):
                phi[j] -= phi[j] // i

    return sum(phi[2 : limit + 1])


if __name__ == "__main__":
    print(solution())
