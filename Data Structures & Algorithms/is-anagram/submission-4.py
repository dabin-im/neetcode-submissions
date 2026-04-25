class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1
        
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1

        for ch in s:
            if ch not in t_map.keys():
                return False
                
            if t_map[ch] != s_map[ch]:
                return False

        return True
        