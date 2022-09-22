

def solution(n=12):
    for a in range(300):
        for b in range(a + 1, 400):
            for c in range(b + 1, 500):
                if (a + b + c) == 1000:
                    if (a**2) + (b**2) == (c**2):
                        return a*b*c

    return -1

def solution2():
    for a in range(300):
        for b in range(400):
            c = 1000 - a - b
            if a < b < c and (a**2) + (b**2) == (c**2):
                return a * b * c
    return -1

if __name__ =='__main__':
    print(solution2())