
def fib(n:int):
    if n <=2 :return 1
    p, q  = 1, 1
    for i in range(3,n+1):
        p, q = q, p+q
    return q


def solution(digit:int= 3)-> int:
    i = 1
    while True:
        if len(str(fib(i))) == digit:
            break
        i+=1
    return i, fib(i)




if __name__ == '__main__':
    print(solution())
    print(solution(1000))