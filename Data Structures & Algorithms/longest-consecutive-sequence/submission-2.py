class Solution:
    """
    Find the length of the longest consecutive sequence in an array.
    
    Example:
        Input: nums = [2,20,4,10,3,4,5]
        Output: 4
        Explanation: The longest consecutive sequence is [2, 3, 4, 5].
    
    Approach:
        - Use a set for O(1) lookups.
        - For each number, only start counting if it's the beginning
          of a sequence (i.e., n-1 is not in the set).
        - Then extend the sequence by checking if the next number exists.
        
    Time: O(n), Space: O(n)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest