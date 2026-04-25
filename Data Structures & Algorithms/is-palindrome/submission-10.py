class Solution:
    def isAlphaNum(self, ch: str) -> bool:
        return ((ch >= 'a' and ch <= 'z') or 
        (ch >= 'A' and ch <= 'Z') or
        (ch >= '0' and ch <= '1'))

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1

            while l < r and not self.isAlphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
        