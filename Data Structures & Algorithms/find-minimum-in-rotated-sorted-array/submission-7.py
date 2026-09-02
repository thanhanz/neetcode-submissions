class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right, res = 0, len(nums) - 1, 1001
        
        if len(nums) < 3:
            return min(nums[left], nums[right])

        while (left < right):
            mid = left + (right - left) // 2
            res = min(nums[mid], res)
                
            if nums[left] <= nums[mid] <= nums[right]: # Not rotated
                res = min(nums[left], res)
                return res
            else: # Find not rotated
                if nums[left] <= nums[mid]:
                    left = mid + 1
                    res = min(nums[left], res)
                else:
                    right = mid - 1
                    res = min(nums[right], res)
        return res