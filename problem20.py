
from math import factorial


def solution(n):
    num = factorial(n)
    r = 0
    while num!=0:
        r = r + num% 10
        num = num //10
    return r



if __name__ == '__main__':
    print(solution(10))
    print(solution(100))
