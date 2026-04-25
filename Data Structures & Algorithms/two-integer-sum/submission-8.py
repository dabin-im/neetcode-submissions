class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_map = {}

        for i, n in enumerate(nums):
            k = target - n

            if k in n_map.keys():
                return [n_map[k], i]
            
            n_map[n] = i

        return []