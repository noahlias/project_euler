## algorithm time complexity O(sqrt(N))
def solution(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    prime = 1
    i = 2
    while i * i <= n:
        while n % i == 0:
            prime = i
            n //= i
        i += 1
    if n > 1:
        prime = n
    return int(prime)


if __name__ == "__main__":
    print(solution(6008514751433212321321))
