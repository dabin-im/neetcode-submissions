class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)

        for n in nums:
            seq = 0
            if n - 1 not in nums:
                seq += 1
                while n + 1 in nums:
                    seq += 1
                    n += 1
                
                longest = max(longest, seq)

        return longest