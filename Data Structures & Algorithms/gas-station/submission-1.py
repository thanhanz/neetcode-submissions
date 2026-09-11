class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # sum(cost) > sum(gas): return -1
        # find start posible index -> Remove Brute Force O(n^2) time complexity
        # Greedy: find start index -> no need to recalculate again -> O(n) time complexity
        if len(gas) != len(cost):
            return -1

        if sum(cost) > sum(gas):
            return -1

        cur_gas, start = 0, 0
        for i in range(len(gas)):
            cur_gas += gas[i] - cost[i]
            if cur_gas < 0:
                start = i + 1
                cur_gas = 0
                continue

        return start