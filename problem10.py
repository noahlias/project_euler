import math


def solution(n=2000000):
    i = 3
    ans = 0
    while i<n:
        if isprime(i):
            ans += i
        i += 1
    return ans
         

def isprime(n):
    if 1 < n < 4:
        # 2 and 3 are primes
        return True
    elif n < 2 or n % 2 == 0 or n % 3 == 0:
        # Negatives, 0, 1, all even numbers, all multiples of 3 are not primes
        return False

    # All primes number are in format of 6k +/- 1
    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

if __name__ == "__main__":
    #print(isprime(4))
    #print(solution(10))
    #print(solution(10))
    print(solution())
