def solution():
    """Get the solution

    Digit cancelling fractions
    """
    numerator = denominator = 1
    for i in range(10, 100):
        for j in range(10, 100):
            if (
                j % 10 != 0
                and i / j < 1
                and i / j == ((i // 10) / (j % 10))
                and i % 10 == (j // 10)
            ):
                numerator = numerator * (i // 10)
                denominator = denominator * (j % 10)
    print(numerator, denominator)


if __name__ == "__main__":
    solution()
