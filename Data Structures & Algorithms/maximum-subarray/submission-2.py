class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -10001
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)

            #Break subarray
            if cur_sum < 0:
                cur_sum = 0

        return max_sum