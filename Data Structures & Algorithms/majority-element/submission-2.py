class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        maxCount = 0

        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1     
    
        return int(max(counts, key=counts.get))