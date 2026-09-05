class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backTrack(temp_list, start, remain):
            if remain == 0:
                result.append(temp_list[:])
                return
            
            for i in range(start, len(candidates)):
                # Prevent duplicated case (in sorted array only)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remain:
                    break

                temp_list.append(candidates[i])
                backTrack(temp_list, i + 1, remain - candidates[i])
                temp_list.pop()
    
        backTrack([], 0, target)
        return result