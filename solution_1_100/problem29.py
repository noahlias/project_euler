def solution():
    """_summary_

    Returns:
        _type_: _description_
    """
    d = set()
    for i in range(2, 101):
        for j in range(2, 101):
            d.add(i**j)
    return len(d)


if __name__ == "__main__":
    print(solution())
