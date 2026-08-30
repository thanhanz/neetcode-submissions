class Solution:
    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]: # Sorted in left part (min -> max)
            if nums[left] <= target <= nums[mid]:
                return self.binarySearch(nums, target, left, mid - 1)
            else: 
                return self.binarySearch(nums, target, mid + 1, right)
        else:                       # Sorted in right part (min -> max)
            if nums[mid] <= target <= nums[right]:
                return self.binarySearch(nums, target, mid + 1, right)
            else:
                return self.binarySearch(nums, target, left, mid - 1)

        

    def search(self, nums: List[int], target: int) -> int:
        
        return self.binarySearch(nums, target, 0, len(nums) - 1)
        
        # Declare a function that store (left, right):
        # Compare with mid = left + (right - left) // 2
        
        # First, find where is the rotated part (But in SORTED status): in left part or right part
        # -> compare sorted in left part or right part 
        # (left < middle => left part SORTED)
        # ELSE:
        # (mid < right => right part SORTED)

        # In each SORTED part we will binarySearch with (left, mid - 1) or (mid + 1, right)
