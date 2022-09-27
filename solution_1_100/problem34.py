from math import factorial

DIGIT_FACTORIAL = {str(d): factorial(d) for d in range(10)}


def solution():
    """_summary_

    Returns:
        _type_: _description_
    """
    limit = 7 * factorial(9) + 1
    return sum(
        i for i in range(3, limit) if sum(DIGIT_FACTORIAL[d] for d in str(i)) == i
    )


if __name__ == "__main__":
    print(solution())
