#!/usr/bin/env python3
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
    min_num_coins = [float('inf')] * (total + 1)
    min_num_coins[0] = 0

    if total == 0:
        return 0
    if total < 0:
        return -1

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                new_min_coin = min_num_coins[amount - coin] + 1
                if min_num_coins[amount] > new_min_coin:
                    min_num_coins[amount] = new_min_coin

    if min_num_coins[total] == float('inf'):
        return -1
    else:
        return min_num_coins[total]
