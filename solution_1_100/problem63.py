def solution() -> int:
    """How many n-digit positive integersexist which are also an nth power

    Formula (9**n) == n
    Returns:
        _type_: _description_
    """
    count = 0
    ans = []
    for i in range(1, 21 + 1):
        j = 9
        while len(str(j**i)) == i and j**i > 0:
            ans.append(f"{j}**{i}")
            count += 1
            j -= 1
    return count


if __name__ == "__main__":
    print(solution())
