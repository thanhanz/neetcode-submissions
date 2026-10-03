class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        match = set()

        for triplet in triplets:
            # Skip triplet that contains value > target items
            x, y, z = triplet
            if x > target[0] or y > target[1] or  z > target[2]:
                continue

            for i, v in enumerate(triplet):
                if v == target[i]:
                    match.add(i)

        return len(match) == 3