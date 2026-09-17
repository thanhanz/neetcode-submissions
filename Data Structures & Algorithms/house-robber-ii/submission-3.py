class Solution:
    def rob(self, nums: List[int]) -> int:

        def robHouse1(nums):
            dp = [0] * len(nums)
            
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

            return dp[-1]

        n = len(nums)
        if not nums:
            return 0
            
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        # Slice first index
        nums_exclude_first = nums[1:n]

        # Slice last index
        nums_exclude_last = nums[:n - 1]
        return max(robHouse1(nums_exclude_first), robHouse1(nums_exclude_last))

        
        