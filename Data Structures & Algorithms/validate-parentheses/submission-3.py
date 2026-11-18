class Solution:
    def isValid(self, s: str) -> bool:
        p = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []

        for i in range(len(s)):
            if s[i] in p:
                stack.append(p[s[i]])
            else:
                if not stack or stack[-1] != s[i]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0
        

        