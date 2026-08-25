class Solution:
    def trap(self, height: List[int]) -> int:
        # # Rain Water Trapping Problem
        # # Algorithm: Two-pass approach to find max heights on left and right of each position
        # # Time: O(n), Space: O(n)
        # # 
        # # Key insight: Water trapped at position i = min(maxLeft[i], maxRight[i]) - height[i]
        # # The water level at any position is determined by the shorter of the two "walls" 
        # # (max height to its left and max height to its right)
        
        # maxl = 0
        # maxr = 0
        # maxLeft = [0] * len(height)   # maxLeft[i] = max height from index 0 to i
        # maxRight = [0] * len(height)  # maxRight[i] = max height from index i to end
        # storage = []
        
        # # First pass: Build maxLeft array (left to right)
        # # At each position, track the maximum height seen so far
        # for i in range(len(height)):
        #     maxl = max(maxl, height[i])
        #     maxLeft[i] = maxl
        
        # # Second pass: Build maxRight array (right to left)
        # # At each position, track the maximum height seen so far from the right
        # for i in range(len(height)-1, -1, -1):
        #     maxr = max(maxr, height[i])
        #     maxRight[i] = maxr

        # # Third pass: Calculate water trapped at each position
        # # Water at position i = min(left_max, right_max) - current_height
        # # Example: if left_max=2, right_max=3, height[i]=0 → water trapped = min(2,3) - 0 = 2 units
        # # If height[i] >= min(left_max, right_max), no water can be trapped (negative amount → 0)
        # for i in range(len(height)):
        #     storage.append(max(0, (min(maxLeft[i], maxRight[i]) - height[i])))
            
        # return sum(storage)

        if not height: return 0

        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]

        storage = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                storage += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                storage += rightMax - height[r]
        
        return storage






