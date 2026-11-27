class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for st in strs:
            text = [0] * 26 
            for ch in st:
                text[ord(ch) - ord('a')] += 1

            res[tuple(text)].append(st)

        return list(res.values())


