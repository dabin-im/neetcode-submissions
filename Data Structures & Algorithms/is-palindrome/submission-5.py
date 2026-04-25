class Solution:
    def isAlphaNum(self, s: str):
        return (s >= '0' and s <= '9' or
                s >= 'a' and s <= 'z' or
                s >= 'A' and s <= 'Z')

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            while not self.isAlphaNum(s[l]) and l < r:
                l += 1
            
            while not self.isAlphaNum(s[r]) and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True