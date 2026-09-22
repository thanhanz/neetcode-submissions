class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Start with "(" with left will add "(" and right will add ")"
        # If open < close or open > n => break that branch (return)
        

        result = []
        parentheses_options = "("
        open = 1
        close = 0
        
        def backTrack(parentheses_options, open, close, n, result):
            if open < close or open > n:
                return

            backTrack(parentheses_options + "(", open + 1, close, n, result)

            backTrack(parentheses_options + ")", open, close + 1, n, result)
            
            if len(parentheses_options) == n * 2:
                result.append(parentheses_options)
                return

        backTrack(parentheses_options, open, close, n, result)
        return result