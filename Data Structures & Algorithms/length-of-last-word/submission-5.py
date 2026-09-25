class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start, end = -1, -1

        for i in range(len(s)-1, -1, -1):
            if end == -1 and s[i] == " ":
                continue
            elif s[i] != " " and end == -1:
                end = i
            elif end != -1 and s[i] == " ":
                start = i + 1
                break
        else:
            start = 0
        
        return end - start + 1