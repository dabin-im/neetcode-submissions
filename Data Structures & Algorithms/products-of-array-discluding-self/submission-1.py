class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums = nums + [1]
        res = [1] * (len(nums) - 1)

        prev = 1
        for i in range(len(res)):
            prev = prev * nums[i - 1]
            res[i] = prev
        
        prev = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] = res[i] * prev
            prev = prev * nums[i] 

        return res