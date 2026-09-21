class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        # Min heap by default
        # Functions in heapq: 
        # - heapq.heapify(arrays)
        # - heapq.heappush(arrays, value)
        # - heapq.heappop(arrays)

        ## Max heap
        # heapq.heappush(heap, -x)
        # x = -heapq.heappop(heap)

        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        top = -max_heap[0]
        while len(max_heap) > 1:
            top = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            remaining = top - second
            if remaining > 0:
                heapq.heappush(max_heap, -remaining)

        return -max_heap[0] if len(max_heap) > 0 else 0