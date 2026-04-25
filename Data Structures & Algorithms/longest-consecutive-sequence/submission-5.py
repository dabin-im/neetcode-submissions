class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for n in nums:
            temp = 1
            while n - 1 in nums:
                temp += 1
                n -= 1

            res = max(temp, res)
        
        return res
            