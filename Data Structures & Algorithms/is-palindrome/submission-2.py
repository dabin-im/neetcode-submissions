class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if not self.isAlphanumeric(s[l]):
                l += 1
                continue
            if not self.isAlphanumeric(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True

    def isAlphanumeric(self, ch: str) -> bool:
        if (ch >= 'a' and ch <= 'z' or
            ch >= 'A' and ch <= 'Z' or
            ch >= '0' and ch <= '9'):
            return True
        else:
            return False