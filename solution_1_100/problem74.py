from math import factorial

FACTORIAL_DICT = {str(i): factorial(i) for i in range(10)}


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
    int_data = sum(FACTORIAL_DICT.get(i) for i in str(n))
    data = {}
    data[n] = 1
    while count > 0 and int_data not in data:
        data[int_data] = 1
        int_data = sum(FACTORIAL_DICT.get(i) for i in str(int_data))
        count += 1
    return len(data.keys())


if __name__ == "__main__":
    print(convert_number(169))
    print(convert_number(871))
    print(convert_number(872))
    print(convert_number(69))
    print(convert_number(78))
    print(solution(60))
    # print(convert_number(540))
