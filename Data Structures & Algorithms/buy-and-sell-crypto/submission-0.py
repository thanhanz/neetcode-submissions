class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPf = 0
        minPrice = prices[0]

        for price in prices:
            maxPf = max(maxPf, price - minPrice)
            minPrice = min(price, minPrice)

        return maxPf