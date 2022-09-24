from sympy import isprime
from typing import List


def solution(n:int= 100)->List[int]:
    ans = []
    for i in range(2,n+1):
        if all(is_prime(i) for i in rotation(i)):
            ans.append(i)
    return ans

def rotation(n:int):
    '''
    >>> 197
    >>> [197,971,719]
    '''
    s = str(n)
    return [ int("".join(s[i:]+s[:i])) for i in range(len(s))]

def is_prime(n):
    '''
    >>>
    '''
    i =2
    while i*i <=n:
        if n%i == 0:
            return False
        i+=1
    return True

if __name__ == "__main__":
    print(rotation(197))
    print(solution())
    print(len(solution(1_000_000)))
