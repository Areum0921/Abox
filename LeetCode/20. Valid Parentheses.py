class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False



