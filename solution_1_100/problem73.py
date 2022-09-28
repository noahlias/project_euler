from math import gcd


def solution(n: int = 8) -> int:
    """Counting fractionss in range

    Time Complexity O(n*(n-1))
    3/8 2/5 3/7
    >>> solution(8)
    >>> 3
    """
    denominator = n
    count = 0
    ans = []
    while denominator > 0:
        for numerator in range(1, denominator + 1):
            if (
                numerator / denominator > 1 / 3
                and numerator / denominator < 1 / 2
                and gcd(numerator, denominator) == 1
            ):
                ans.append((numerator, denominator))
                count += 1
        denominator -= 1
    return count


if __name__ == "__main__":
    print(solution(8))
    print(solution(1000))
    print(solution(12_000))
