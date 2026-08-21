class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1] * len(nums)
        postfixProduct = [1] * len(nums)

        productPre = 1
        for i in range(len(nums)):
            prefixProduct[i] = productPre
            productPre *= nums[i]

        productPos = 1
        for i in range(len(nums) - 1, -1, -1):
            postfixProduct[i] = productPos
            productPos *= nums[i]

        output = []
        for i in range(len(nums)):
            output.append(prefixProduct[i] * postfixProduct[i])

        return output