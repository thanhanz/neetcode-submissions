class Solution:
    def climbStairs(self, n: int) -> int:
    # Look like Fibonanci
        prev = 0
        cur = 1

        for _ in range(n):
            prev, cur = cur, prev + cur

        return cur