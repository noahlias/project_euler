def solution(digit: int = 4):
    """Solution

    9^5 = 59049
    59049 * 7 = 413343 (which is only 6 digit number)
    So, numbers greater than 999999 are rejected
    and also 59049 * 3 = 177147 (which exceeds the criteria of number being 3 digit)
    So, number > 999
    and hence a number between 1000 and 1000000
    """
    ans = []
    for i in range(2, 10**6):
        if judge(i, digit):
            ans.append(i)
    return sum(ans), ans


def judge(n: int, digit: int = 4):
    """_summary_

    Args:
        n (int): _description_
        digit (int, optional): _description_. Defaults to 4.

    Returns:
        _type_: _description_
    """
    ## can store the pow 1-9 digit as a  dict to avoid calculate repeat.
    total = sum(pow(i, digit) for i in map(int, list(str(n))))
    if total == n:
        return True
    else:
        return False


if __name__ == "__main__":
    # print(solution()) #(19316, [1634, 8208, 9474])
    print(solution(5))
