class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]

        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            bucket[c].append(n)

        res = []
        for array in reversed(bucket):
            for ele in array:
                if len(res) == k:
                    return res
                res.append(ele)


        return res