class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) < 2:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        # This must be max of two number -> solve case [2, 1, 1, 2] -> 4
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]