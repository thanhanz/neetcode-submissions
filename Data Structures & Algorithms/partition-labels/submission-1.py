class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result, mp = [], {}
        
        # Create storing max position of each unique characters
        # mp = {
        #    'a': last_position,
        #    'b': last_position,
        #    ...
        # }
        for i, char in enumerate(s):
            # Override last index
            mp[char] = i

        start_sub = 0
        end_sub = -1

        for i, char in enumerate(s):
            end_sub = max(mp[char], end_sub)

            if i == end_sub:
                result.append(end_sub - start_sub + 1)
                start_sub = i + 1
        
        return result
            

