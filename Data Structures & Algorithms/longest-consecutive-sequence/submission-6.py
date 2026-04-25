class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)

        for n in nums:
            temp = 1
            while n + 1 in nums:
                temp += 1
                n += 1

            res = max(temp, res)

        return res