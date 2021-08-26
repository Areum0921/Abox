class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        climbing = [0] * (n + 1)
        climbing[1] = 1
        climbing[2] = 2

        for i in range(3, n + 1):
            climbing[i] = climbing[i - 1] + climbing[i - 2]

        return climbing[n]