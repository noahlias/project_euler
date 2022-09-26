LETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTER_DICT = dict(zip(list(LETTER), range(1, 27)))


def solution():
    """This is a solution for problem 22.

    Using names.txt (right click and 'Save Link/Target As...'),
    a 46K text file containing over five-thousand first names,
    begin by sorting it into alphabetical order.
    hen working out the alphabetical value for each name,
    multiply this value by its alphabetical position
    in the list to obtain a name score.
    For example, when the list is sorted into alphabetical order,
    COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
    is the 938th name in the list.
    So, COLIN would obtain a score of 938 × 53 = 49714.
    """
    with open("data/p022_names.txt", "r") as f:
        data: str = f.read()
    data = data.replace('"', "").split(",")
    data.sort()
    # print(data)
    # print(data.index('COLIN'))
    num_scores = 0
    for index, value in enumerate(data):
        if index == 937:
            print((index + 1) * sum(LETTER_DICT.get(j) for j in value))
        num_scores += (index + 1) * sum(LETTER_DICT.get(j) for j in value)
    return num_scores


if __name__ == "__main__":
    print(sum(LETTER_DICT.get(j) for j in "COLIN"))
    print(solution())
