class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        nums = nums + [1]

        prev = 1
        for i in range(len(res)):
            res[i] = prev * nums[i - 1] 
            prev = res[i]
        print(res)
        prev = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] = prev * res[i] 
            prev = prev * nums[i]

        return res