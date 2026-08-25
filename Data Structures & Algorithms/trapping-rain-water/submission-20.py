# RAIN WATER TRAPPING PROBLEM
# Trap rainwater between elevation bars
# Example: height = [0,1,0,2,1,0,1,3,2,1,2,1] → 6 units trapped

from typing import List

# ============================================================================
# ALTERNATIVE APPROACH (commented): TWO ARRAYS (O(n) time, O(n) space)
# ============================================================================
# Core Idea:
# At each position i, water trapped = min(maxLeft[i], maxRight[i]) - height[i]
# The water level is limited by the SHORTER of the two "walls" (left max, right max)
#
# Example trace with height = [0,1,0,2,1,0,1,3,2,1,2,1]:
#   Position 2: maxLeft[2]=1, maxRight[2]=3, height[2]=0
#              water = min(1,3) - 0 = 1 unit ✓
#   Position 5: maxLeft[5]=2, maxRight[5]=3, height[5]=0
#              water = min(2,3) - 0 = 2 units ✓
#
# def trap_two_arrays(self, height: List[int]) -> int:
#     if not height:
#         return 0
#     
#     n = len(height)
#     
#     # maxLeft[i] = maximum height from index 0 to i (inclusive)
#     maxLeft = [0] * n
#     maxLeft[0] = height[0]
#     for i in range(1, n):
#         maxLeft[i] = max(maxLeft[i-1], height[i])
#     
#     # maxRight[i] = maximum height from index i to end (inclusive)
#     maxRight = [0] * n
#     maxRight[n-1] = height[n-1]
#     for i in range(n-2, -1, -1):
#         maxRight[i] = max(maxRight[i+1], height[i])
#     
#     # At each position, calculate trapped water
#     # Water level at i = min(maxLeft[i], maxRight[i])
#     # Water trapped = water level - bar height
#     water = 0
#     for i in range(n):
#         water_level = min(maxLeft[i], maxRight[i])
#         water += water_level - height[i]
#     
#     return water

# ============================================================================
# MAIN SOLUTION: TWO POINTERS (O(n) time, O(1) space) - OPTIMAL
# ============================================================================

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        water = 0
        
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]
        
        return water


# ============================================================================
# HOW THE MAIN SOLUTION WORKS (TWO POINTERS)
# ============================================================================
# Core Idea:
# Instead of storing max heights, track them on-the-fly with two pointers.
# KEY INSIGHT: We only need to know the MINIMUM of the two maxes.
#
# Why this works:
# If leftMax < rightMax, we KNOW rightMax ≥ leftMax
# So the water level at position l is DEFINITELY determined by leftMax
# (rightMax is taller, so it doesn't limit us)
# Therefore: water_at_l = leftMax - height[l]
#
# Example trace with height = [0,1,0,2,1,0,1,3,2,1,2,1]:
#
# Initial state:
#   l=0 (leftMax=0), r=11 (rightMax=1)
#   leftMax < rightMax? YES → process left side
#   l=1, leftMax=max(0,1)=1, water += 1-1=0
#   Continue until leftMax becomes bottleneck...
#   
# Position 2:
#   l=2, height[2]=0, leftMax=1
#   water += 1-0=1 ✓ (1 unit trapped!)
#
# Why we can trust leftMax at position 2:
#   We haven't touched right side yet, but we KNOW rightMax ≥ 2 (there's a 3)
#   So water level = min(1, ≥2) = 1 ← determined by leftMax alone
#
# The bottleneck logic:
#   - If leftMax < rightMax: left side determines water level (move left)
#   - If rightMax <= leftMax: right side determines water level (move right)


# ============================================================================
# COMPARISON
# ============================================================================
# Approach 1 (Two Arrays):
#   ✓ Easier to understand conceptually
#   ✓ Clearly shows maxLeft[i] and maxRight[i] for each position
#   ✗ Uses O(n) extra space for two arrays
#
# Approach 2 (Two Pointers):
#   ✓ O(1) space - only track two variables (leftMax, rightMax)
#   ✓ Single pass (though not truly single - it's a two-way pass)
#   ✗ Less obvious why the logic works (need to understand bottleneck concept)
#   ✗ Harder to debug visually
#
# BOTH have O(n) time complexity


# ============================================================================
# DETAILED EXECUTION TRACE - TWO POINTER APPROACH
# ============================================================================
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Index:  0 1 2 3 4 5 6 7 8 9 10 11
#
# INITIAL: l=0, r=11, leftMax=0, rightMax=1, water=0
#
# Iteration 1: leftMax(0) < rightMax(1)? YES → move LEFT
#   l=1, leftMax=max(0,height[1])=max(0,1)=1
#   water += 1 - 1 = 0  [bar height equals water level, no trap]
#   Total water: 0
#
# Iteration 2: leftMax(1) < rightMax(1)? NO → move RIGHT
#   r=10, rightMax=max(1,height[10])=max(1,2)=2
#   water += 2 - 2 = 0  [bar height equals water level, no trap]
#   Total water: 0
#
# Iteration 3: leftMax(1) < rightMax(2)? YES → move LEFT
#   l=2, leftMax=max(1,height[2])=max(1,0)=1
#   water += 1 - 0 = 1  ✓ TRAP 1 UNIT!
#   [Height is 0, water level is 1, so 1 unit fills it]
#   Total water: 1
#
# Iteration 4: leftMax(1) < rightMax(2)? YES → move LEFT
#   l=3, leftMax=max(1,height[3])=max(1,2)=2
#   water += 2 - 2 = 0  [bar height equals water level]
#   Total water: 1
#
# Iteration 5: leftMax(2) < rightMax(2)? NO → move RIGHT
#   r=9, rightMax=max(2,height[9])=max(2,1)=2
#   water += 2 - 1 = 1  ✓ TRAP 1 UNIT!
#   Total water: 2
#
# ... (similar iterations continue)
#
# Eventually: leftMax=2, rightMax=3
# When we process position 5 from left:
#   water += 2 - 0 = 2  ✓ TRAP 2 UNITS!
#   [Height is 0, water level is 2 (limited by leftMax, rightMax is 3)]
#   Total water: 6 ✓ CORRECT!


# ============================================================================
# WHY THE BOTTLENECK LOGIC WORKS
# ============================================================================
#
# The two-pointer algorithm relies on this principle:
#
# If leftMax < rightMax, then for position 'left':
#   The water level = min(leftMax, rightMax) = leftMax
#
# Why? Because:
#   1. We've scanned from left and found leftMax is the max we've seen
#   2. We haven't processed positions between 'left' and 'right' yet
#   3. But we KNOW rightMax exists and is > leftMax
#   4. So whatever happens in the middle, rightMax will be there
#   5. Therefore, water at 'left' can NEVER exceed leftMax
#   6. We can safely calculate: water = leftMax - height[left]
#
# This avoids needing to store all maxLeft and maxRight values upfront!
# We only need to track the CURRENT maxes and let the bottleneck tell us
# which side to process next.