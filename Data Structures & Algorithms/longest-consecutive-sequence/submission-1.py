class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use sets here as we can easily check if element exists for O(1)
        numSet = set(nums)
        longest = 0 
        for n in numSet:
            # Check if its the start of the sequence
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
