from typing import List


def solution():
    """_summary_

    Returns:
        _type_: _description_
    """
    return coin_change_sum(200, [1, 2, 5, 10, 20, 50, 100, 200])


def coin_change_sum(money: int, detail_coins: List[int]) -> int:
    """Coin change sum get answer

    >>> coin_change_sum(200)
    >>> 73682
    Args:
        money (int): _description_
        detail_coins (List[int]): _description_

    Returns:
        int: _description_
    """
    dp = [0] * (money + 1)
    dp[0] = 1
    for i in detail_coins:
        for j in range(i, money + 1):
            dp[j] += dp[j - i]
    return dp[-1]


if __name__ == "__main__":
    print(solution())
