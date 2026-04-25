class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countM = {}
        res = []
        for n in nums:
            countM[n] = countM.get(n, 0) + 1

        bucket = [[] for i in range(len(nums) + 1)]

        for key, value in countM.items():
            bucket[value].append(key)


        for i in range(len(bucket) - 1, -1, -1):
            for item in bucket[i]:
                if k == len(res):
                    break
                else:
                    res.append(item)
        
        return res