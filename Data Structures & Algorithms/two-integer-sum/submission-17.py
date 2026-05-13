class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {}

        for i in range(len(nums)):
            k = target - nums[i]
            
            if k in nMap:
                return [nMap[k], i]
            
            nMap[nums[i]] = i

        
        return []
