class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for str in strs:
            key = "".join(sorted(str))

            if key not in map:
                map[key] = [str]
                continue
            
            map[key].append(str)
        
        return list(map.values())

            
            
            

