class Solution:
    """
    Encodes and decodes a list of strings.

    Strategy: Use a length-prefix encoding.
    Each string is encoded as:
        <length_of_string>#<string>
    
    Example 1:
        Input:  ["Hello", "World"]
        Encode: "5#Hello5#World"
        Decode: ["Hello", "World"]

    Example 2:
        Input:  ["", "ab", "c"]
        Encode: "0#2#ab1#c"
        Decode: ["", "ab", "c"]

    Key points:
    - The "#" character acts as a delimiter between the length and the string.
    - During decoding, we read the length, then jump ahead by that many
      characters to extract the string.
    - This handles strings with any characters (spaces, symbols, etc.)
      because we know exactly how many characters each string occupies.
    """

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            # Find the '#' delimiter to know where the length ends
            j = i
            while s[j] != "#":
                j += 1
            
            # Extract the length (characters between i and j, exclusive of j)
            lengthOfWord = int(s[i:j])
            
            # Extract the word: start right after '#', take 'lengthOfWord' chars
            res.append(s[j + 1 : j + 1 + lengthOfWord])
            
            # Move i to the start of the next length prefix
            i = j + 1 + lengthOfWord
        
        return res