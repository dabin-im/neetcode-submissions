class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        bucket = [[] for i in range(len(nums) + 1)]
        res = []

        for i in range(len(nums)):
            num_count[nums[i]] = num_count.get(nums[i], 0) + 1

        for key, value in num_count.items():
            bucket[value].append(key)

        print(bucket)

        for i in range(len(bucket) - 1, -1, -1):
            for item in bucket[i]:
                res.append(item)
                
                if k == len(res):
                    return res

        return res
