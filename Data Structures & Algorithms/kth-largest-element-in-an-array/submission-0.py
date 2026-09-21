class Solution:
    def findKthLargest(self, nums: List [int], k: int) -> int:
        # Using max heap and heapq.pop() "k" times
        # Remember heapq.heapify() is void function
        import heapq

        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        while k > 1:
            heapq.heappop(max_heap)
            k -= 1

        return -max_heap[0]