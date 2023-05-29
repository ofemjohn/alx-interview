#!/usr/bin/python3
'''taking turns with prime numbers from a set of integers'''


def isWinner(x, nums):
    ''' Returns:
    name of the player that won the most rounds.
    If the winner cannot be determined, return None.
    '''
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_won = 0
    ben_won = 0

    for num in nums:
        if num == 1:
            ben_won += 1
        elif is_prime(num) and num > 2:
            maria_won += 1
        else:
            ben_won += 1

    if maria_won > ben_won:
        return "Maria"
    elif ben_won > maria_won:
        return "Ben"
    else:
        return None
