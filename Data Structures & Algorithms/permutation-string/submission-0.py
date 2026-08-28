class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False
        
        # alphabet have 26 letters (a - z)
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        # ord('a') = 97 => because all are lowercase letters
        for i in range(n1):
            s1_freq[ord(s1[i]) - 97] += 1
            s2_freq[ord(s2[i]) - 97] += 1

        if s1_freq == s2_freq:
            return True
        
        for i in range(n1, n2):
            s2_freq[ord(s2[i]) - 97] += 1
            s2_freq[ord(s2[i - n1]) - 97] -= 1
            if s1_freq == s2_freq:
                return True

        return False
            