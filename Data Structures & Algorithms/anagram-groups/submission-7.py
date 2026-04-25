class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            c_arr = [0] * 26
            for ch in s:
                c_arr[ord(ch) - ord('a')] += 1
            
            m[tuple(c_arr)].append(s)

        return m.values()
