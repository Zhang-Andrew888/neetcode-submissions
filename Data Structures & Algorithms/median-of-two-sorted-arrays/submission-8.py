class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2

        if len(nums1) > len(nums2):
            a = b
            b = nums1
        
        total = len(a) + len(b)
        half = total // 2

        l, r = 0, len(a) - 1

        while True:
            i = (l + r) // 2 # A
            j = half - i - 2# B: index of midpoint

            Aleft = a[i] if i >= 0 else float("-infinity")
            Aright = a[i + 1] if (i + 1) < len(a) else float("infinity")
            Bleft = b[j] if j>=0 else float("-infinity")
            Bright = b[j + 1] if (j+1) < len(b) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2 == 1:
                    return min(Aright, Bright)

                # even
                return (max(Aleft, Bleft) + min(Bright, Aright)) / 2
            elif Aleft > Bright: 
                r = i -1
            else:
                l = i + 1
