class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # [-1,0,1,2,-1,-4]
        # [-4, -1, -1, 0, 1, 2] at that time: nlog(n), space complexity: O(n)

        for i in range(len(nums)):
            if nums[i] > 0:
                break
                
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            # define indices
            j = i + 1
            k = len(nums) - 1

            # [-4, -1, -1, 0, 1, 2]
            #      i       j,    k 

            while j < k:
                # define numbers for summation
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    print(res)

                    j += 1
                    k -= 1
                    while nums[j - 1] == nums[j] and j < k:
                        j += 1

                   

        return res
            
