class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, n in enumerate(nums):
            k = target - n
            
            if k in mp.keys():
                return[mp[k], i]
            
            mp[n] = i

        return []