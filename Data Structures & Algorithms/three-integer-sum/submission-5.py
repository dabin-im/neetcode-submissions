class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums.sort()
        
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    if not [nums[i], nums[j], nums[k]] in res:
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        
        return res