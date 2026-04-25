class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        
        for n in nums:
            if n - 1 not in nums:
                length = 1
                k = n + 1
                while k in nums:
                    length += 1
                    k += 1
                longest = max(longest, length) 

        return longest