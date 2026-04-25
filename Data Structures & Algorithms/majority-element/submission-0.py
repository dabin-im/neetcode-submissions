class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        mcnt, key = 0, 0
        for n in nums:
            res[n] = res.get(n, 0) + 1

        for k in res.keys():
            if mcnt < res[k]:
                mcnt = res[k]
                key = k
        
        return key