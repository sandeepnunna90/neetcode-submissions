class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        i = 0

        while i < len(s)-1: 
            total += abs(ord(s[i+1]) - ord(s[i]))
            i += 1

        return total

