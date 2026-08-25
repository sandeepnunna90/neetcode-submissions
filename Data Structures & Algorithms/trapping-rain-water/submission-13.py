class Solution:
    def trap(self, height: List[int]) -> int:
        # Uses O(n) time, O(n) space as well
        # The algo is that at every position (the index is of length 1 (the whole block)) we calculate the max height of the blocks on its left and right. 
        maxl = 0
        maxr = 0
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        storage = []
        

        for i in range(len(height)):
            maxl = max(maxl, height[i])
            maxLeft[i] = maxl
            
        
        for i in range(len(height)-1, -1, -1):
            maxr = max(maxr, height[i])
            maxRight[i] = maxr

        for i in range(len(height)):
            # image left is 2 and right is 3. but the height at your positon 
            # of h[i] = 0 -> you can store 2 units of water
            # if h[i] = 1 -> you can only store 1 unit of water

            # diff = min(maxLeft[i], maxRight[i]) - height[i]
            # if diff < 0: 
            #     water = 0
            storage.append(max(0, (min(maxLeft[i], maxRight[i]) - height[i])))
            
        return sum(storage)
