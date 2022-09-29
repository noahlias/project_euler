from math import factorial


def solution(terms: int) -> int:
    """Get the solution

    Args:
        terms (int): _description_

    Returns:
        int: _description_
    """
    return sum(1 for i in range(1, 1_000_000 + 1) if convert_number(i) == terms)


def convert_number(n: int):
    """Produces a chain of five non-repeating terms

    Args:
        n (int): _description_
        terms (int, optional): _description_. Defaults to 60.

    Returns:
        _type_: _description_
    """
    count = 1
    int_data = sum(factorial(int(i)) for i in str(n))
    data = set()
    data.add(n)
    while count > 0 and int_data not in data:
        data.add(int_data)
        int_data = sum(factorial(int(i)) for i in str(int_data))
        count += 1
    return len(data)


if __name__ == "__main__":
    print(convert_number(169))
    print(convert_number(871))
    print(convert_number(872))
    print(convert_number(69))
    print(convert_number(78))
    print(solution(60))
    # print(convert_number(540))
