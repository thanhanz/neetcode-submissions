class Solution:
    # def backTrack(self, nums: List[int], target: int, result: List[int], tempList: List[int]) -> List[List[int]]:
    #     for num in nums:
    #         tempList.append(num)
    #         if sum(tempList) <= target:
    #             if sum(tempList) == target:
    #                 if sorted(tempList) not in result:
    #                     result.append(list(sorted(tempList)))
    #                 tempList.pop()
    #                 continue
    #             #Compare sum with target to prevent 'Max recursion depth exceeded'
    #             self.backTrack(nums, target, result, tempList)

    #         tempList.pop()
                
    # Eliminate because Time Limit Issue happen when array too long
            

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, temp_list = [], []
        n = len(nums)

        def backTrack(i, cur_sum):
            # Define basecase
            if cur_sum == target:
                result.append(temp_list[:])
                return

            if cur_sum > target or i == n:
                return

            # Go to not pick branch
            backTrack(i + 1, cur_sum)

            # Go to pick branch
            temp_list.append(nums[i])
            backTrack(i, cur_sum + nums[i])
            temp_list.pop()

        backTrack(0, 0)
        return result