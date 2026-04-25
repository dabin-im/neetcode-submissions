class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for st in strs:
            s_arr = [0] * 26

            for ch in st:
                s_arr[ord(ch) - ord('a')] += 1

            res[tuple(s_arr)].append(st)

        return res.values()
            