class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        target = n - 1
        # n - 1 -> 0: (-1)
        for i in range(n - 1, -1, -1):
            max_jump = nums[i]
            if i + max_jump >= target:
                target = i
            
        return target == 0 