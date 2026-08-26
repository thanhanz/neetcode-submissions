class Solution:

    def getMaxValueInDict(self, map: {}) -> int:
        maxKey = max(map, key=map.get)
        maxVal = map[maxKey]
        return maxVal

    def characterReplacement(self, s: str, k: int) -> int:
        left, maxLength, maxFreq = 0, 0, 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            maxFreq = self.getMaxValueInDict(freq)

            windowSize = right - left + 1

            if (windowSize - maxFreq > k):
                freq[s[left]] = freq.get(s[left]) - 1
                left += 1
            
            #Recaculate again the window length
            windowSize = right - left + 1
            maxLength = max(maxLength, windowSize)
        
        return maxLength