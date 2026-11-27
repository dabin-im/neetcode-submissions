class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        bucket = [[] for i in range(len(nums) + 1)]
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for n, f in counts.items():
            bucket[f].append(n)

        for items in reversed(bucket):
            for n in items:
                if len(res) < k:
                    res.append(n)
                else:
                    return res
                    
        return res