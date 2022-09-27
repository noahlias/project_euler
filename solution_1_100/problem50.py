def is_prime(n):
    """Judge whether a number is prime

    >>> is_prime(2)
    >>> True
    """
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def solution(n: int):
    """_summary_

    >>> solution(100)
    >>> 41
    >>> solution(1000)
    >>> 953
    Args:
        n (int): _description_
    """
    i = 2
    count = 0
    ans = []
    total = 0
    while True:
        if is_prime(i):
            total += i
            if total > n:
                break
            ans.append(total)
        i += 1
    ans = [0] + ans
    print(ans)
    for i in range(len(ans)):
        for j in range(i + 1, len(ans)):
            if is_prime(ans[j] - ans[i]):
                if j - i == 543:
                    print(j, i, ans[j] - ans[i])
                count = max(count, j - i)
    return count


if __name__ == "__main__":
    print(solution(100))
    print(solution(1_000))
    print(solution(1_000_000))
