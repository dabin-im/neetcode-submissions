class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            alpha_array = [0] * 26
            for ch in word:
                alpha_array[ord(ch) - ord('a')] += 1
            
            hashmap[tuple(alpha_array)].append(word)

        return list(hashmap.values())