

def BuySellStock(prices):
    buy = prices[0]
    profit = 0

    for i in range(1,len(prices)):
        if buy > prices[i]:
            buy = prices[i]
        
        elif prices[i] - buy > profit:
            profit = prices[i] - buy
    return profit



print(BuySellStock([7,1,5,3,6,4]))
print(BuySellStock([7,6,4,3,2,1]))
print(BuySellStock([1]))
print(BuySellStock([2,4,1]))
print(BuySellStock([3,2,6,5,0,3]))


