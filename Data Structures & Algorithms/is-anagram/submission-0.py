class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for char in s:
            if char not in count_s:
                count_s[char] = 1
            else: 
                count_s[char] += count_s[char]
        
        for char in t:
            if char not in count_t:
                count_t[char] = 1
            else: 
                count_t[char] += count_t[char]

        return (count_s == count_t)