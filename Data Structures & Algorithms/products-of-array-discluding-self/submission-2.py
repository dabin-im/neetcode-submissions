class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        nums = nums + [1]

        prev = 1
        for i in range(len(res)):
            prev = prev * nums[i - 1]
            res[i] = prev

        print(res)

        prev = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] = prev * res[i]
            prev = prev * nums[i]

        print(res)

        return res


