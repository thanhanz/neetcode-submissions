import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        map = Counter(hand)
        min_heap = list(map.keys())
        heapq.heapify(min_heap)

        while min_heap:
            top = min_heap[0]
            for i in range(groupSize):
                current = top + i
                if map[current] == 0: # Cannot get current
                    return False
                map[current] -= 1
                # Only pop() when no longer have in hashMap
                if map[current] == 0: 
                    if current != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True

