#!/usr/bin/python3
"""
    makeChange - function to make change
"""
def makeChange(coins, total):
    # If the total is 0 or less, no coins are needed
    if total <= 0:
        return 0
    
    # Create a list to store the fewest coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0
    
    # Loop over each coin and update the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, it's not possible to make that total
    return dp[total] if dp[total] != float('inf') else -1
