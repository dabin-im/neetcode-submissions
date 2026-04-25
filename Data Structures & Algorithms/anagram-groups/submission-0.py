class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            ch_arr = [0] * 26
            for ch in s:
                ch_arr[ord(ch) - ord('a')] += 1
            res[tuple(ch_arr)].append(s)
            
        return res.values()

