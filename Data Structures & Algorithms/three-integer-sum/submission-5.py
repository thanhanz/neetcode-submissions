class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        # If array we will need two loop to prevent duplicate
        result = set()
        nums.sort()

        #[-4, -1, -1, 0, 1, 2]
        for i in range(len(nums) - 2):
            target = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = target + nums[left] + nums[right]

                if total == 0:
                    result.add((nums[left], nums[right], target))
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
            
        return [list(x) for x in result]
                

                




        