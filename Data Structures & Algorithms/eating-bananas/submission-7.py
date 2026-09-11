import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:



        minRate, maxRate = 1, max(piles)
        # h is max hours available to eat

        res = maxRate
        while minRate <= maxRate:
            mid = (minRate + maxRate) // 2

            totalHours = 0

            for pile in piles:
                # we are doing this to round up as we don't have ciel function here. 
                # 5/2 = 2.5  ---> // this round it to 2 but ciel rounds it to 3, we need math library
                # so we are using the below logic to always round up properly. 
                totalHours += ((pile + mid - 1) // mid)
            

            if totalHours > h:
                minRate = mid + 1
            
            elif totalHours <= h:
                res = min(res, mid)
                maxRate = mid - 1

        return res