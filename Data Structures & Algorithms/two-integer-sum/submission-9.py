class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, n in enumerate(nums):
            k = target - n
            if k in m.keys():
                return [m[k], i]
            m[n] = i

        return []
