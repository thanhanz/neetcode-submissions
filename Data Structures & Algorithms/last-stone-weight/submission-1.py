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

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            remaining = x - y
            if remaining > 0:
                heapq.heappush(max_heap, -remaining)

        return -max_heap[0] if len(max_heap) > 0 else 0