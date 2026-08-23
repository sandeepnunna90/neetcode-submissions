class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # BRUTE Force --> This would do time limit exceeded if j starts with i+1
        # result = 0

        # for i in range(0, len(heights)): 
        #     for j in range(i+1, len(heights)): 
        #         area = (j-i) * min(heights[i], heights[j])
        #         result = max(result, area)
        
        # return result

        res = 0
        l, r = 0, len(heights)-1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(area, res)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
            

    

