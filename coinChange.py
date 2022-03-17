def coinChange(coins, amount):
    dp = [amount+1] * (amount +1)
    dp[0] = 0

    for i in range(len(dp)):
        for coin in coins:
            if (i < coin):
                continue
            # iterate over all coin to find the min
            dp[i] = min(dp[i], 1+dp[i-coin])
    if (dp[amount] == amount+1):
        return -1
    else:
        return dp[amount]

if __name__ == "__main__":
    coins = [2, 3]
    amount = 3
    print(coinChange(coins, amount))
