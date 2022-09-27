def solution(s: str, k: int):
    """_summary_

    Args:
        s (str): _description_
        k (int): _description_

    Returns:
        _type_: _description_
    """
    product_max = 0
    for index, _ in enumerate(s):
        product_max = max(product_max, product_number(int(s[index : index + k])))
    return product_max


def product_number(number):
    """_summary_

    Args:
        number (_type_): _description_

    Returns:
        _type_: _description_
    """
    ans = 1
    while number != 0:
        ans *= number % 10
        number = number // 10
    return ans


if __name__ == "__main__":
    with open("data/p08_data.txt", "r") as f:
        sequence_series = f.read()
    print(solution(sequence_series, 13))
    print(product_number(1234))
