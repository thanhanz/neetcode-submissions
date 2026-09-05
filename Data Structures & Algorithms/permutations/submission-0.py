class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backTrack(temp_list):
            if len(temp_list) == n:
                result.append(temp_list[:])
                return
            
            for i in range(n):
                if nums[i] in temp_list:
                    continue

                temp_list.append(nums[i])
                backTrack(temp_list)
                temp_list.pop()
        
        backTrack([])
        return result