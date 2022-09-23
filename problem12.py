def solution():
    #res = []
    tNum = 1
    i = 1

    while True:
        i += 1
        tNum += i ## sum(n) = sum(n-1) + n
        #print(tNum)
        if divisor_count(tNum) > 500:
            break

    return tNum


def divisor_count(n):
    i = 2
    count = 1
    while i*i <= n: # O(sqrt(n))
        multiplicity = 0
        while n%i == 0:
            n//=i
            multiplicity += 1
        count *= multiplicity + 1
        i+=1
    if n>1:
        count *=2
    return count


if __name__ =='__main__':
    print(solution())
    #print(divisor_count(25))
