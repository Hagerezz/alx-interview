#!/usr/bin/python3
"""
    function to count money
"""
def makeChange(coins, total):
    """
        function to count money
    """
    if total <= 0:
        return 0
    else:
        coins = sorted(coins)
        coins.reverse()
        c = 0
        for i in coins:
            while total >= i:
                c += 1
                total -= i
        if total == 0:
            return c
        return -1
