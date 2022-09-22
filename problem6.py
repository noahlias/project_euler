

def solution(n=100):
    sum_of_the_squares = sum(i*i for i in range(1,n+1))
    ## another solution
    ## sum_of n  is  sum(i for i in range(1,n+1))
    ## square_of_sum = sum_of_n* sum_of_n
    ## 1**2+2**2+....+n**2 = n(n+1)(2n+1)//6 this is a formula 
    square_of_sum = n*(n+1)*n*(n+1)//4
    return square_of_sum - sum_of_the_squares


if __name__ == '__main__':
    print(solution(10))
    print(solution(100))
