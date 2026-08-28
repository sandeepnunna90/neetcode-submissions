class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                j += 1
                i += 1
            elif t[j] != s[i]:
                j += 1
            
        return i == len(s)