def solution():
    """Max powerful digit sum

    Returns:
        _type_: _description_
    """
    max_powerful_digit_sum = 0
    res = []
    for i in range(1, 101):
        for j in range(1, 101):
            if digit_sum(i**j) >= max_powerful_digit_sum:
                max_powerful_digit_sum = digit_sum(i**j)
                res.append((i, j, i**j))
    return max_powerful_digit_sum, res[-1]


def digit_sum(n: int):
    """Simple digit sum

    Args:
        n (int): _description_

    Returns:
        _type_: _description_
    """
    return sum([int(i) for i in str(n)])


if __name__ == "__main__":
    print(solution())
    print(max([digit_sum(i**j) for i in range(1, 101) for j in range(1, 101)]))
