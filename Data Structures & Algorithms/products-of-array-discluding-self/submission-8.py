class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        nums += [1]
        prev = 1
      
        for i in range(len(res)):
            res[i] = nums[i - 1] * prev
            prev = res[i]

        prev = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= prev
            prev *= nums[i]

        return res
        

