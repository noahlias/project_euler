def solution():
    """_summary_

    Returns:
        _type_: _description_
    """
    tNum = 1
    i = 1

    while True:
        i += 1
        tNum += i
        if divisor_count(tNum) > 500:
            break

    return tNum


def divisor_count(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    i = 2
    count = 1
    while i * i <= n:
        multiplicity = 0
        while n % i == 0:
            n //= i
            multiplicity += 1
        count *= multiplicity + 1
        i += 1
    if n > 1:
        count *= 2
    return count


if __name__ == "__main__":
    print(solution())
    # print(divisor_count(25))
