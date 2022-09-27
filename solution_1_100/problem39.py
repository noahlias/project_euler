def solution(n: int = 1000) -> int:
    """Integer right triangles

    Returns perimeter with maximum solutions.
    >>> Solution()
    >>> 840
    Args:
        n (int, optional): _description_. Defaults to 1000.

    Returns:
        int: _description_
    """
    data = {i: find_solution(i) for i in range(1, n + 1)}
    max_values = max(data.values())
    for k, v in data.items():
        if v == max_values:
            return k


def find_solution(n: int) -> int:
    """Find all solution

    Formula
    a**a + b**b = c**c
    a + b +c = n
    >>> find_solution(120)
    >>> 3
    """
    count = 0
    for i in range(1, n // 3 + 1):
        for j in range(i, n // 2 + 1):
            if i * i + j * j == (n - i - j) * (n - i - j):
                count += 1
    return count


if __name__ == "__main__":
    # print(find_solution(120))
    print(solution())
