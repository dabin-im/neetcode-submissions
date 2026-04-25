class Solution:
    def isValid(self, s: str) -> bool:
        h_map = {'(' :')', '[' :']', '{' :'}'}
        stack = []

        for ch in s:
            if ch in h_map:
                stack.append(ch)
            
            else:
                if len(stack) == 0:
                    return False

                pop_str = stack.pop()

                if h_map[pop_str] != ch:
                    return False
        
        return len(stack) == 0

        