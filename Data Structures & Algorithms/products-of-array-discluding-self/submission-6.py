# from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         """
#         Algorithm:
#         1. prefixProduct[i] = product of all nums[0..i-1]
#            - productPre starts at 1
#            - prefixProduct[i] = productPre
#            - then productPre *= nums[i]

#         2. postfixProduct[i] = product of all nums[i+1..n-1]
#            - productPos starts at 1
#            - postfixProduct[i] = productPos
#            - then productPos *= nums[i]

#         3. output[i] = prefixProduct[i] * postfixProduct[i]

#         Time:  O(n) — three linear passes
#         Space: O(n) — two extra arrays of size n
#         """
#         n = len(nums)

#         prefixProduct = [1] * n
#         postfixProduct = [1] * n

#         productPre = 1
#         for i in range(n):
#             prefixProduct[i] = productPre
#             productPre *= nums[i]

#         productPos = 1
#         for i in range(n - 1, -1, -1):
#             postfixProduct[i] = productPos
#             productPos *= nums[i]

#         output = []
#         for i in range(n):
#             output.append(prefixProduct[i] * postfixProduct[i])

#         return output




from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Visual walkthrough for nums = [1, 2, 4, 6]:

        1) nums:    [1, 2, 4, 6]

        2) prefix:  product of all values left of i
                    [1, 1, 2, 8]

        3) postfix: product of all values right of i
                    [48, 24, 6, 1]

        4) output:  prefix[i] * postfix[i]
                    [48, 24, 12, 8]

        Time:  O(n) — one pass for prefix, one pass for postfix
        Space: O(1) extra space — output array not counted toward extra space
        """
        n = len(nums)
        output = [1] * n   # will store prefix products first

        # Prefix pass: output[i] = product of nums[0..i-1]
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]

        # Postfix pass: multiply each output[i] by product of nums[i+1..n-1]
        postfix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output