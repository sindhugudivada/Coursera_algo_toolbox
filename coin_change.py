# Uses python3
import sys

def get_change(m):
    coins = [1,3,4]
    return min_coins(coins,m)

# Recursive Version Approach
def min_coins(coins,m):
    solution = float("inf")
    if m in coins:
        return 1
    if m < min(coins):
        return 0
    for coin in coins:
        solution = min(solution,1 + (min_coins(coins, m-coin)))

    return solution

# Dynamic Programming Approach
def min_coins(coins,m):
    cache = [float("inf")] * (m+1)
    cache[0] = 0
    if m < min(coins):
       cache[m] = 0
    for amount in range(min(coins),m+1):
        for coin in coins:
            if amount in coins:
                cache[amount] = 1
            else:
                cache[amount] = min(cache[amount],1 + cache[max(0,amount-coin)])
    return cache[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
