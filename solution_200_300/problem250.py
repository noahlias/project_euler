def compute(n=250):
    """_summary_

    Args:
        n (int, optional): _description_. Defaults to 250.

    Returns:
        _type_: _description_
    """
    # Use dynamic programming
    MOD = 10**16
    subsets = [0] * n
    # subsets[i] is {the number of subsets with sum equal to i mod 250} mod 10^16
    subsets[0] = 1
    for i in range(1, 200000 + 1):
        offset = pow(i, i, n)
        # print(offset)
        subsets = [
            (val + subsets[(j - offset) % n]) % MOD for (j, val) in enumerate(subsets)
        ]
    print(subsets)
    ans = (subsets[0] - 1) % MOD
    return str(ans)


def solution():
    """_summary_

    Get the solution
    """
    m = 250
    mm = 10**16
    x = m * [0]

    for i in range(1, 250251):
        x[pow(i, i, m)] += 1

    print(x)
    y = [1] + (m - 1) * [0]

    for i in range(m):
        for j in range(x[i]):
            y = [(y[k] + y[(k - i) % m]) % mm for k in range(m)]
    print(y[0] - 1)


if __name__ == "__main__":
    # print(compute())
    solution()
