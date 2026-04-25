class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = len(strs[0])
        for st in strs:
            min_length = min(min_length, len(st))
        
        res = ''
        for i in range(min_length):
            ch = strs[0][i]
            for k in range(1, len(strs)):
                if ch != strs[k][i]:
                    return res
            
            res += ch

        return res