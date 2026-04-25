class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while not self.isAlphanumeric(s[l]) and l < r:
                l += 1
            while not self.isAlphanumeric(s[r]) and l < r:
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l, r = l + 1, r - 1
        
        return True

    def isAlphanumeric(self, ch: str) -> bool:
        if (ch >= 'a' and ch <= 'z' or
            ch >= 'A' and ch <= 'Z' or
            ch >= '0' and ch <= '9'):
            return True
        else:
            return False
   