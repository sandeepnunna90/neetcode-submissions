class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}
        
        # This solution has O(s+t) Time complexity 
        # and O(s+t) for spac
        for char in s:
            if char not in count_s:
                count_s[char] = 1
            else: 
                count_s[char] += 1
        for char in t:
            if char not in count_t:
                count_t[char] = 1
            else: 
                count_t[char] += 1

        return (count_s == count_t)