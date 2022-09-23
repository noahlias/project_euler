
def solution(numerator: int = 3, denominator: int = 7, limit: int = 1000000):
    max_numerator = 0
    max_denominator = 1

    for current_denominator in range(1, limit + 1):
        current_numerator = current_denominator * numerator // denominator
        if current_denominator % denominator == 0:
            current_numerator -= 1
        if current_numerator * max_denominator > current_denominator * max_numerator:
            max_numerator = current_numerator
            max_denominator = current_denominator
    return max_numerator, max_denominator


if __name__ == '__main__':
    print(solution(numerator=3, denominator=7, limit=1000000))