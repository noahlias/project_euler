def solution(digit:int):
    max_product = 0
    for i in range(1,10**digit):
        for j in range(1,10**digit):
            if str(i*j) == str(i*j)[::-1]:
                max_product = max(max_product,i*j)
    return max_product

def solution1(digit:int):
    pass

if __name__ == '__main__':
    print(solution(4))