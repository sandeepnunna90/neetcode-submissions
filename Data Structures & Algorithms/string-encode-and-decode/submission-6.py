class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            lengthOfWord = int(s[i:j]) # string start and stop (won't include end value as it start from 0)
            res.append(s[j + 1 : j + 1 + lengthOfWord])
            i = j + 1 + lengthOfWord
        
        return res