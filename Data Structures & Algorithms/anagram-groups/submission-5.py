class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for st in strs:
            ch_arr = [0] * 26

            for ch in st:
                ch_arr[ord(ch) - ord('a')] += 1
            
            hashMap[tuple(ch_arr)].append(st)

        return hashMap.values()