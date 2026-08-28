class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        charMap = {"[" : "]",
                   "(" : ")", 
                   "{" : "}"}
        stack = []

        for i in range(len(s)):
            if s[i] in charMap:
                stack.append(s[i])
            else:
                if not stack:
                    return False

                top = stack.pop()
                if charMap[top] != s[i]:
                    return False
        
        if not stack:
            return True

        return False
