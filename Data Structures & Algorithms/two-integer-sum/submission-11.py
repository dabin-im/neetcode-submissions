class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_map = {}

        for i in range(len(nums)):
            k = target - nums[i]
            if k in n_map:
                return [n_map[k], i]

            n_map[nums[i]] = i
        
        return []
