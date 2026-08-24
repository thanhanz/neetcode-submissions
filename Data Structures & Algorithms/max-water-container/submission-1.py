class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        result = -1

        while (left < right):
            water_stored = min(heights[left], heights[right]) * (right - left)
            result = max(result, water_stored)

            if (heights[left] < heights[right]):
                left += 1
                continue
            else:
                right -= 1
                continue

        return result