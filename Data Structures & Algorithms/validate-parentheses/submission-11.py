class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for ch in s:
            if ch in closeToOpen and len(stack) > 0:
                if closeToOpen[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        print(len(stack))
        return len(stack) == 0