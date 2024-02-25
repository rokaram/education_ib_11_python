def remain_coins(coins):
    return oct(coins)[2]


coins = int(input("Enter the number of coins: "))
print(remain_coins(coins))
