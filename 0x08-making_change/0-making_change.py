#!/usr/bin/python3
'''
Returns the fewest number of coins needed to meet a given amount total.

  Args:
    coins: A list of the values of the coins in your possession.
    total: The amount of money to make change for.

  Returns:
    The fewest number of coins needed to meet total.
    If total is 0 or less, returns 0.
    If total cannot be met by any number of coins you have, returns -1.
'''


def makeChange(coins, total):
    '''returns fewest number of coins needed to meet total.'''
    if total == 0:
        return 0
    count = 0
    index = 0
    sorted_coins = sorted(coins, reverse=True)
    length = len(coins)
    while total > 0:
        if index >= length:
            return -1
        if total - sorted_coins[index] >= 0:
            total -= sorted_coins[index]
            count += 1
        else:
            index += 1
    return count
