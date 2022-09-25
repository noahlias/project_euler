def solution():
    max_powerful_digit_sum = 0
    res = []
    for i in range(1,101):
        for j in range(1,101):
            if digit_sum(i**j)>= max_powerful_digit_sum:
                max_powerful_digit_sum = digit_sum(i**j)
                res.append((i,j, i**j))
    return max_powerful_digit_sum,res[-1]

def digit_sum(n:int):
    return sum([int(i) for i in str(n)])

if __name__ == '__main__':
    print(solution())
    print( max([ digit_sum(i**j) for i in range(1,101) for j in range(1,101)]))