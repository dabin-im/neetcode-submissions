class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1

        for key, val in m.items():
            freq[val].append(key)

        for items in reversed(freq):
            for item in items:
                if k == len(res):
                    break
                
                res.append(item)

        return res
                