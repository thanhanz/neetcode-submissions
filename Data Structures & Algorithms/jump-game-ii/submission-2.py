class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # Greedy - DP
        # Time: O(n)
        # Space: O(1)

        # Separate into REGIONS (with max jump can reach to) -- far
        # end -- mark the end of region 
        # (i == e) mean you need to jump right now 

        far, end, smallest_jump = 0, 0, 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])

            if i == end:
                end = far
                smallest_jump += 1

        return smallest_jump