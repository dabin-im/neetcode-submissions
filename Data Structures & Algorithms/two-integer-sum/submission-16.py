class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            k = target - nums[i]

            if k in m:
                return [m[k], i]

            m[nums[i]] = i

        return []