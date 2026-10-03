class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
            
        min_p = max_p = nums[0]
        result = -1
        
        for num in nums[1:]: #Skip first value
            temp = min_p
            min_p = min(num, min_p * num, max_p * num) 
            max_p = max(num, temp  * num, max_p * num)

            result = max(result, max_p)

        return result
        