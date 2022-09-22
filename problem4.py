def solution(digit:int):
    max_product = 0
    for i in range(10**digit-1,99, -1):
        for j in range(10**digit-1,99, -1):
            if str(i*j) == str(i*j)[::-1]:
                max_product = max(max_product,i*j)
    return max_product

def solution1(n: int = 998001):
    for number in range(n - 1, 9999, -1):
        str_number = str(number)
        if str_number == str_number[::-1]:
            divisor = 999
            while divisor != 99:
                if (number % divisor == 0) and (len(str(number // divisor)) == 3.0):
                    return number
                divisor -= 1

if __name__ == '__main__':
    print(solution(3))
    #print(solution1())
