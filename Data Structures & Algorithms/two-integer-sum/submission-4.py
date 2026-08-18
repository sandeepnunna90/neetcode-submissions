class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff not in prevMap:
                prevMap[n] = i
            else:
                return [prevMap[diff], i]
