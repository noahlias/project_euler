import math


def solution(n=10001):
    cnt = 0
    i = 2
    res = []
    while i>1:
        if isprime(i) and cnt<n:
            res.append(i)
            cnt+=1
        elif cnt >=n:
            break
        i += 1
    return res[-1]
         

def isprime(n):
    i= 2
    while i<=math.sqrt(n):
        if n%i ==0:
            return False
        i+=1
    return True

if __name__ == "__main__":
    #print(isprime(22))
    #print(solution(10))
    print(solution())