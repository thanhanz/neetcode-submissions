class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result, mp = [], {}
        
        # Create storing max position of each unique characters
        for i in range(len(s) - 1, -1, -1):
            mp[s[i]] = max(mp.get(s[i], 0), i)

        # 
        start_sub = 0
        max_position = -1
        for i in range(len(s)):
            max_position = max(mp.get(s[i]), max_position)
            
            if mp.get(s[i]) < max_position:
                continue

            if i == max_position:
                sub_len = max_position - start_sub + 1
                start_sub = i + 1
                result.append(sub_len)

        return result
            

