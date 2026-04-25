class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # [-1,0,1,2,-1,-4]
        # [-4, -1, -1, 0, 1, 2] at that time: nlog(n), space complexity: O(n)

        for i in range(len(nums) - 2):
            # define indices
            j = i + 1
            k = len(nums) - 1

            # [-4, -1, -1, 0, 1, 2]
            #           i,, k   jk 

            while j < k:
                # define numbers for summation
                n1 = nums[i]
                n2 = nums[j]
                n3 = nums[k]

                if n1 + n2 + n3 > 0 and j < k:
                    k -= 1
                elif n1 + n2 + n3 < 0 and j < k:
                    j += 1
                else:
                    if [n1, n2, n3] not in res:
                        res.append([n1, n2, n3])
                    k -= 1
                    j += 1

        return res
            
