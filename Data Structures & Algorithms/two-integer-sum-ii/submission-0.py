class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        result = []
        while (left < right):
            sum = numbers[left] + numbers[right]
            if (sum == target):
                result.append(left + 1)
                result.append(right + 1)
                return result

            if (sum < target):
                left += 1
                continue
            elif (sum > target):
                right -= 1
                continue
        return result
        
            
