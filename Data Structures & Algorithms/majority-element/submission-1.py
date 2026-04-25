class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        m_cnt = 0
        key = 0

        for n in nums:
            res[n] = res.get(n, 0) + 1

            if m_cnt < res[n]:
                m_cnt = res[n]
                key = n
                
        return key