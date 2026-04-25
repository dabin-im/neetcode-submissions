class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        arr = [[] for i in range(len(nums) + 1)]
        res = []
        for n, c in count.items():
            arr[c].append(n)

        for row in reversed(arr):
            for item in row:
                if k == 0:
                    return res

                res.append(item)
                k -= 1

        return res
