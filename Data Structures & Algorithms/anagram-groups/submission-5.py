class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} # mapping charCount to list of anagrams
        
        for s in strs: 
            count = [0] * 26 # a..z

            for c in s:
                count[ord(c) - ord("a")] += 1

            # count is an array with 26 elements 
            # each element corresponds to a charter count
            # count of abc would be [1, 1, 1, 0, 0 .....] all other 0 
            # are until 26th elemen

            # we should convert array to tuple in python
            # as it CAN'T DO array as keys   { [1,2,3]: "sssss" } NOT OK
            # we can do tuple as key instead { (1,2,3): "sssss" } OK
            
            countT = tuple(count)

            if countT not in result:
                result[countT] = [s]
            else: 
                result[countT].append(s)

        
        return list(result.values())