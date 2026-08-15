class Solution:
    # Using HEAP (maxHeap/minHeap) -> timeComplexity: O(nlogn)


    # Using bucket -> timeComplexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        #Init size for bucket
        bucket = [[] for _ in range(len(nums) + 1)]
        
        #Create hashMap
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for key, val in freq_map.items():
            bucket[val].append(key)

        i = len(bucket) - 1
        res = []
        while (i >= 0):
            if bucket[i]:
                for num in bucket[i]:
                    res.append(num)
                
                if len(res) == k:
                    return res
            i -= 1
