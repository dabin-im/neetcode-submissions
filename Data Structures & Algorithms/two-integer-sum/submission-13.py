class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, n in enumerate(nums):
            k = target - n
            if k in res.keys():
                return [res[k], i]
            
            res[n] = i

        return []