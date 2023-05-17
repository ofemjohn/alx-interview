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
    if total < 0:
        return -1
    min_num_coins = [float('inf')] * (total + 1)
    min_num_coins[0] = 0

    for coin in coins:
        # Update the fewest number of coins needed for
        # each value from the current coin value to total
        for value in range(coin, total + 1):
            if min_num_coins[value - coin] != float('inf'):
                min_num_coins[value] = min(
                    min_num_coins[value], 1 + min_num_coins[value - coin])
    # If the fewest number of coins needed for
    #  the total is still infinity, it means it
    #  cannot be met by any number of coins
    if min_num_coins[total] == float('inf'):
        return -1

    # Return the fewest number of coins
    # needed for the total
    return min_num_coins[total]
