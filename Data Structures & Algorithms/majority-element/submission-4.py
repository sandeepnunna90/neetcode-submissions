class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counts = defaultdict(int)
        # maxCount = 0

        # for i in range(len(nums)):
        #     if nums[i] in counts:
        #         counts[nums[i]] += 1
        #     else:
        #         counts[nums[i]] = 1     
    
        # return max(counts, key=counts.get)
        
        # ----------------------------
        
        # Majority Element logic here is that it occurs
        # more than n/2 times. The below logic works then.

        count = 0
        res = 0

        for n in nums:
            if res == n: 
                count += 1
            elif res != n and count > 0:
                count -= 1
            elif res != n and count == 0:
                res = n
        
        return res
