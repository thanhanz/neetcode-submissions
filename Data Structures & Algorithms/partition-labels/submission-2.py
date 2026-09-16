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

        # start_sub = 0
        end_sub = -1

        # Can use a variable size instead
        size = 0
        # when index change -> size++
        # index == max_sub -> result.append(size) and reset size = 0

        for i, char in enumerate(s):
            size += 1
            end_sub = max(mp[char], end_sub)

            if i == end_sub:
                # result.append(end_sub - start_sub + 1)
                result.append(size)
                # start_sub = i + 
                size = 0
        
        return result
            

