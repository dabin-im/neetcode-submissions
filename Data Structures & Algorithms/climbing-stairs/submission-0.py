class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        next = 1
        
        for i in range(n, 0, -1):
            temp = next
            next = next + prev
            prev = temp

            print(next, prev)

        return next