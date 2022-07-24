class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l = 0
        h = len(nums1) - 1

        while True:
            a_part = (l + h) // 2
            b_part = half - a_part - 2

            a_left_max = nums1[a_part] if a_part >= 0 else float("-infinity")
            a_right_min = nums1[a_part + 1] if (a_part + 1) < len(nums1) else float("infinity")
            b_left_max = nums2[b_part] if b_part >= 0 else float("-infinity")
            b_right_min = nums2[b_part + 1] if (b_part + 1) < len(nums2) else float("infinity")

            if a_left_max <= b_right_min and b_left_max <= a_right_min:
                if total % 2:
                    return min(a_right_min, b_right_min)
                return (max(a_left_max, b_left_max) + min(a_right_min, b_right_min)) / 2
            elif a_left_max > b_right_min:
                h = a_part - 1
            else:
                l = a_part + 1
                
                
#TC = O(log(m+n))
#SC = O(1)
