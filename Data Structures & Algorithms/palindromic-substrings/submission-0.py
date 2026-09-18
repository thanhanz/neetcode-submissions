class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        # Iterating each characters, every character we will find odd/even case
        # Odd: a | x | a -> x would be anything
        # Event: a, b | b, a -> check the next of that
        
        for i in range(len(s)):
            # Odd case (left == right)
            count += self.countPalindromes(s, i, i)
            
            # Even case (s[left] == s[left + 1])
            count += self.countPalindromes(s, i, i + 1)
        return count

    def countPalindromes(self, s, left, right):
        count = 0

        while (left >= 0 and right < len(s) and s[left] == s[right]):
            count += 1
            left -= 1
            right += 1

        return count
            