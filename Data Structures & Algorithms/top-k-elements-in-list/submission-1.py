class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for n, c in counts.items():
            buckets[c].append(n)

        print(buckets)
        res = []
        for arr in reversed(buckets):
            for n in arr:
                res.append(n)
                if len(res) == k:
                    return res
           
        return res