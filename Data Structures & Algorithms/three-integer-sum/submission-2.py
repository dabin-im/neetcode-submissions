class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum_res = nums[i] + nums[j] + nums[k]
                if sum_res < 0:
                    j += 1
                elif sum_res > 0:
                    k -= 1
                else:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return res