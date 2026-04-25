class Solution:
    def isValid(self, s: str) -> bool:
        pair = {}
        stack = []

        for ch in s:
            if ch == '[':
                pair[ch] = ']'
                stack.append(ch)
            elif ch == '{':
                pair[ch] = '}'
                stack.append(ch)
            elif ch == '(':
                pair[ch] = ')'
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                temp = stack.pop()
                if pair[temp] != ch:
                    return False

        if len(stack) > 0:
            return False

        return True
        