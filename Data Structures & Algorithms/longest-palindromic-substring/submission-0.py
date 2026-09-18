class Solution:
    def longestPalindrome(self, s: str) -> str: 
        if not s or len(s) < 1:
            return ""

        start, end = 0, 0
        for i in range(len(s)):
            # Odd case (left == right)
            maxLenOddCase = self.maxLengthPalindromes(s, i, i)
            
            # Even case (s[left] == s[left + 1])
            maxLenEvenCase = self.maxLengthPalindromes(s, i, i + 1)
            maxLen = max(maxLenOddCase, maxLenEvenCase)
            if maxLen > end - start:
                start = i - ((maxLen - 1) // 2)

                # This works for odd-length palindromes, but not even-length ones -> Remove -1
                end = i + (maxLen // 2)

        return s[start:end + 1]

    def maxLengthPalindromes(self, s, left, right):
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1

        # -1 because it would extra left/right
        return right - left - 1