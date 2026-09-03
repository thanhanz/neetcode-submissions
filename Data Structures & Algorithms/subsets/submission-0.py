class Solution:
    def backTrack(self, res: List[List[int]], tempList: List[int], nums: List[int], start: int):
        res.append(list(tempList))
        for i in range(start, len(nums)):
            tempList.append(nums[i])
            self.backTrack(res, tempList, nums, i + 1)
            tempList.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backTrack(res, [], nums, 0)
        return res

            