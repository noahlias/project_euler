def solution(n:int=10)->int:
    '''
    >>> 1**1+2**2+ 3**3+ 4**4+ 5*
    '''
    return sum(i**i for i in range(1,n))%(10**10)

if __name__ == "__main__":
    print(solution(1000))