class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prev = 1
        
        for i in range(len(res)):
            res[i] = prev
            prev *= nums[i]

        prev = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= prev
            prev *= nums[i]

        return res
