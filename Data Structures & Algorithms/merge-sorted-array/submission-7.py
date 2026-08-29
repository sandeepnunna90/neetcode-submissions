class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        counter = m + n - 1  #(last index of nums1)

        i = m - 1
        j = n - 1
        
        while i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                nums1[counter] = nums2[j]
                j -= 1
            else:
                nums1[counter] = nums1[i]
                i -= 1
            counter -= 1

        # fill in left over elements of nums2 in nums1 as nums2 is already sorted. 
        while j >= 0:
            nums1[counter] = nums2[j]
            j, counter = j - 1, counter - 1
