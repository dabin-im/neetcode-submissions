class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        max_len = 0
        for n in n_set:
            if (n - 1) in n_set:
                continue
            length = 0
            while n in n_set:
                length += 1
                n = n + 1
            
            max_len = max(max_len, length)
        
        return max_len