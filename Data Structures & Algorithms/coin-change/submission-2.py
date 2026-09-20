class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # The case Greedy (Amount -= largest num in array)
        # Case: [1, 5, 6, 9] -> output = 2 (5 + 6), if Greedy it will return 3 (9 + 1 + 1)
        
        dp = [0] * (amount + 1)
        coins.sort()
        for i in range(1, amount + 1):
            minCoin = sys.maxsize

            for coin in coins:
                if i < coin:
                    break
                minCoin = min(minCoin, 1 + dp[i - coin])
            dp[i] = minCoin
        
        # if dp[amount] == sys.maxsize:
        #     return -1
        return dp[-1] if dp[amount] != sys.maxsize else -1
                
            