class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
        # Overwriting the Array here by using a second pointer to start from 0
        # and whenver we need a valid element (number ! = val) we basically are
        # rewriting the array from scracth and pushing that element to k