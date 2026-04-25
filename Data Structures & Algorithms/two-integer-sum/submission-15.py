class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}


        for i in range(len(nums)):
            k = target - nums[i]

            if k in numbers:
                return [numbers[k], i]

            numbers[nums[i]] = i
        return []