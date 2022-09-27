def solution(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    return sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)


if __name__ == "__main__":
    print(solution(10))
    print(solution(1000))
