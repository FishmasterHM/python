#Say you have an array for which the ith element is the price of a given stock on day i.

#If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an #algorithm to find the maximum profit

nums = [7, 1, 5, 3, 6, 4]

def main(nums):
    if len(prices) <= 1:
        return 0
    minp = prices[0]
    maxprofit = 0
    for i in prices:
        maxprofit = max(maxprofit, i - minp)
        minp = min(minp, i)
    return maxprofit



print main(nums)
