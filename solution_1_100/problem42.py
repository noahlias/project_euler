LETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTER_DICT = {k: ord(k) - 64 for k in LETTER}


def solution():
    """Coded triangle numbers

    >>> solution()
    >>> 162
    """
    with open("data/p042_words.txt", "r") as f:
        data = f.read().replace('"', "").split(",")
    return sum(1 for i in data if is_triangle_word(i))


def is_triangle_word(s: str) -> bool:
    """Judge is triangle word

    >>> is_triangle_word('SKY')
    >>> True
    Args:
        s (str): _description_
    """
    value = sum(LETTER_DICT.get(i) for i in s)
    i = 1
    result = 1
    while result <= 26 * 26:
        if result == value:
            break
        i += 1
        result += i
    return result == value


if __name__ == "__main__":
    print(is_triangle_word("SKY"))
    print(solution())
