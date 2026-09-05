class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # max_subset = len(nums)
        result = []
        nums.sort()

        def backTrack(temp_list, start):            
            # if (len(temp_list) < len(nums) + 1) and temp_list not in result:
            result.append(temp_list[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                temp_list.append(nums[i])
                backTrack(temp_list, i + 1)
                temp_list.pop()


        backTrack([], 0)
        return result

            
