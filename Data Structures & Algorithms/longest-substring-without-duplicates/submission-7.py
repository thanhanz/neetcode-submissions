class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        left, result = 0, -1
        map = {}

        for i in range(len(s)):
            if (s[i] in map):
                left = max(left, map[s[i]] + 1)
            
            map[s[i]] = i
            result = max(result, i - left + 1)

        return result
                    
            