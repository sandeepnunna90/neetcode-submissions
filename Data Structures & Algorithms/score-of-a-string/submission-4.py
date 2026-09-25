class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        i = 0

        while i < len(s)-1: 
            total = ord(s[i+1]) - ord(s[i])
            result += abs(total)
            i += 1

        return result

