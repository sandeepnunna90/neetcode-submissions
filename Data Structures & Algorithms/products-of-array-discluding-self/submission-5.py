from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Algorithm:
        1. prefixProduct[i] = product of all nums[0..i-1]
           - productPre starts at 1
           - prefixProduct[i] = productPre
           - then productPre *= nums[i]

        2. postfixProduct[i] = product of all nums[i+1..n-1]
           - productPos starts at 1
           - postfixProduct[i] = productPos
           - then productPos *= nums[i]

        3. output[i] = prefixProduct[i] * postfixProduct[i]

        Time:  O(n) — three linear passes
        Space: O(n) — two extra arrays of size n
        """
        n = len(nums)

        prefixProduct = [1] * n
        postfixProduct = [1] * n

        productPre = 1
        for i in range(n):
            prefixProduct[i] = productPre
            productPre *= nums[i]

        productPos = 1
        for i in range(n - 1, -1, -1):
            postfixProduct[i] = productPos
            productPos *= nums[i]

        output = []
        for i in range(n):
            output.append(prefixProduct[i] * postfixProduct[i])

        return output