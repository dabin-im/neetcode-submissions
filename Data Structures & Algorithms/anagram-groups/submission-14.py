class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word = defaultdict(list)


        for st in strs:
            arr = [0] * 26
            
            for ch in st:
                arr[ord(ch) - ord('a')] += 1

            word[tuple(arr)].append(st)

        return list(word.values())
