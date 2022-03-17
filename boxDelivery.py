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

def boxDelivery(boxes):
    # Count frequency of boxes
    freq = {}
    coins = [2, 3]
    result = 0
    for i in boxes:
        if (i in freq):
            freq[i] += 1
        else:
            freq[i] = 1
    # print(freq)
    for amount in freq.values():
        if amount == 1:
            return -1
        else:
            # print("###" +str(amount))
            num = coinChange(coins, amount)
            if(num==-1):
                return -1
            else:
                result += num
            # print("###"+ str(result))
    return result

if __name__ == "__main__":
    # coins = [1,2,5]
    # amount = 11
    boxes = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
    # boxDelivery(boxes)
    print(boxDelivery(boxes))
    # print(coinChange(coins, amount))