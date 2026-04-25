class Solution:
    def isPali(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            
            l, r = l + 1, r - 1
        return True
        
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(s):
                res.append(subset.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    subset.append(s[i:j + 1])
                    dfs(j + 1)
                    subset.pop()

        dfs(0)
        return res 

