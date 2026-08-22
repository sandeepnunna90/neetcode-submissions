class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        def is_alnum(c: str) -> bool:
            code = ord(c)
            return (
                48 <= code <= 57 or
                65 <= code <= 90 or
                97 <= code <= 122
            )

        # ASCII symbols of 
        while l < r:
            if not is_alnum(s[l]):
                l += 1
                continue
            if not is_alnum(s[r]):
                r -= 1
                continue

            if s[l].lower() == s[r].lower():
                l+= 1
                r-= 1
            else: 
                return False
        return True