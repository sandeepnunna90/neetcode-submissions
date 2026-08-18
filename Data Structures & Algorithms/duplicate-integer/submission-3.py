class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums: 
            if n in count:
                return True
            else:
                count[n] = "exists"
        return False
