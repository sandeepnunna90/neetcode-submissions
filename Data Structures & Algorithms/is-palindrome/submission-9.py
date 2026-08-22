class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two-pointer approach:
        # - l starts at the beginning, r starts at the end.
        # - Skip non-alphanumeric characters by moving l right and r left.
        # - Compare the remaining characters case-insensitively.
        # - If any pair doesn't match, return False.
        # - If the pointers meet/cross, all valid characters matched, so return True.
        l, r = 0, len(s) - 1

        def is_alnum(c: str) -> bool:
            code = ord(c)
            return (
                48 <= code <= 57 or   # digits: ord('0') = 48, ord('9') = 57
                65 <= code <= 90 or   # uppercase: ord('A') = 65, ord('Z') = 90
                97 <= code <= 122     # lowercase: ord('a') = 97, ord('z') = 122
            )

        while l < r:
            if not is_alnum(s[l]):
                l += 1
                continue

            if not is_alnum(s[r]):
                r -= 1
                continue

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True