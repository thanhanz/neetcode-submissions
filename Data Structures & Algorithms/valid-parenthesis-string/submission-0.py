class Solution:
    def checkValidString(self, s: str) -> bool:
        # '*' = '(' || ')' || ""
        
        # Input: ((**), output: true
        # Because * (1) = "", * (2) = ')' => Input turn to (()) => True

        # Input: (((*), output False
        min_open = 0
        max_open = 0

        for ch in s:
            if ch == '(':
                min_open += 1
                max_open += 1

            elif ch == ')':
                min_open -= 1
                max_open -= 1

            else:  # '*'
                min_open -= 1   # treat * as ')'
                max_open += 1   # treat * as '('

            if max_open < 0:
                return False

            min_open = max(min_open, 0)

        return min_open == 0


        
