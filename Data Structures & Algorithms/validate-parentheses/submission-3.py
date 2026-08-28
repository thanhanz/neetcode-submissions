class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        closeToOpen = {"]" : "[",
                       ")" : "(", 
                       "}" : "{" }
        stack = []

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:  # empty stack (dont have close or matching)
                    return False
            else: 
                stack.append(c)

        return not stack # Finally stack must be empty