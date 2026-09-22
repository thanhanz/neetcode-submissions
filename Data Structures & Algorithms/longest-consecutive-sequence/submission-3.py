class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Using sort() and set() -> not the best idea case
        if len(nums) < 1:
            return 0
        
        # nums = list(set(nums))
        # nums.sort()
        # count = 1
        # longest = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1] + 1:
        #         count += 1
        #         longest = max(longest, count)
        #     else:
        #         count = 1
        # return longest

        # ==============================================================
        # Find minValue and use while loop to find others (compare together)

        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s: #This mean we find the minValue of Sub-Consecutive-Sequence
                next_val = num + 1
                length = 1
                while next_val in s:
                    next_val += 1
                    length += 1
                longest = max(longest, length)

        return longest
