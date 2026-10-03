class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # match = set()

        # for triplet in triplets:
        #     # Skip triplet that contains value > target items
        #     x, y, z = triplet
        #     if x > target[0] or y > target[1] or  z > target[2]:
        #         continue

        #     for i, v in enumerate(triplet):
        #         if v == target[i]:
        #             match.add(i)

        # return len(match) == 3

        find = [False] * len(target)
        
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            
            if a == target[0]:
                find[0] = True

            if b == target[1]:
                find[1] = True
                
            if c == target[2]:
                find[2] = True
        
        return True if find[0] and find[1] and find[2] else False
