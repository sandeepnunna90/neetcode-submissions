class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length_of_current_seq = 0
        maxlength_of_seq = 0
        for n in nums:
            if n == 1:
                length_of_current_seq += 1
                if maxlength_of_seq < length_of_current_seq:
                    maxlength_of_seq = length_of_current_seq
            else:
                length_of_current_seq = 0
        return maxlength_of_seq