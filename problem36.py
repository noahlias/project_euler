def solution():
    i = 1
    ans = []
    while i <= 1_000_000:
        if ispalindromes(i) and str(i) == str(i)[::-1]:
            ans.append(i)
        i+=1
    print(ans)
    return sum(ans)

def ispalindromes(n):
    '''
    >>> 585 (1001001001)binary
    >>> True
    '''
    c = bin(n)[2:]
    return c == c[::-1]

if __name__ == "__main__":
    print(ispalindromes(585))
    print(ispalindromes(23))
    print(solution())