# ============================================================
# PREFIX SUM APPROACH
# ============================================================
#
# Goal:
#   Support fast range sum queries:
#   sum(nums[left..right]) inclusive
#
# Idea:
#   Precompute a running total array called prefixSum.
#   prefixSum[i] = sum of all elements from nums[0] to nums[i].
#
# Formula:
#   sumRange(left, right)
#   = prefixSum[right] - prefixSum[left - 1]
#
#   If left == 0, then prefixSum[left - 1] is not valid,
#   so we treat it as 0.
#
# Why this works:
#   prefixSum[right]           = nums[0] + ... + nums[right]
#   prefixSum[left - 1]        = nums[0] + ... + nums[left - 1]
#
#   Difference:
#   nums[left] + ... + nums[right]
#
# Example:
#   nums = [-2, 0, 3, -5, 2, -1]
#
#   After __init__:
#   prefixSum = [-2, -2, 1, -4, -2, -3]
#
#   sumRange(2, 5):
#     prefixSum[5] = -3
#     prefixSum[1] = -2
#     result = -3 - (-2) = -1
#     Actual: 3 + (-5) + 2 + (-1) = -1
#
#   sumRange(0, 2):
#     prefixSum[2] = 1
#     left == 0, so subtract 0
#     result = 1 - 0 = 1
#     Actual: -2 + 0 + 3 = 1
#
#   If left == right:
#     Example: sumRange(3, 3)
#     prefixSum[3] = -4
#     prefixSum[2] = 1
#     result = -4 - 1 = -5
#     Actual: nums[3] = -5
#
# Time Complexity:
#   __init__:  O(n)
#   sumRange:  O(1)
#
# Space Complexity:
#   O(n) for prefixSum
# ============================================================

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        total = 0

        for n in nums:
            total += n
            self.prefixSum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        prefixSumRight = self.prefixSum[right]
        prefixSumLeft = self.prefixSum[left - 1] if left > 0 else 0

        return prefixSumRight - prefixSumLeft

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left, right)