class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)


        for word in strs:
            ch_arr = [0] * 26

            for ch in word:
                ch_arr[ord(ch) - ord('a')] += 1
            
            words[tuple(ch_arr)].append(word)
            
        return list(words.values())