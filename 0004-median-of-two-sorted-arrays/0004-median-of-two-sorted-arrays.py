class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        smaller_list = nums1
        larger_list = nums2

        if len(smaller_list) > len(larger_list):
            smaller_list, larger_list = larger_list, smaller_list

        total_length = len(smaller_list) + len(larger_list)
        half_length = total_length // 2

        left_boundary = 0
        right_boundary = len(smaller_list)

        while True:
            cut_small = (left_boundary + right_boundary) // 2
            cut_large = half_length - cut_small
            
            small_left = smaller_list[cut_small-1] if cut_small > 0 else float ("-infinity")
            small_right = smaller_list[cut_small] if cut_small < len(smaller_list) else float ("infinity")

            large_left = larger_list[cut_large-1] if cut_large > 0 else float ("-infinity")
            large_right = larger_list[cut_large] if cut_large < len(larger_list) else float ("infinity")

            if small_left <= large_right and large_left <= small_right:
                if total_length % 2 != 0:
                    return float(min(small_right, large_right))

                else:
                    max_left = max(small_left, large_left)
                    min_right = min(small_right, large_right)
                    return (max_left + min_right) /2.0

            elif small_left > large_right:
                right_boundary = cut_small - 1

            else:
                left_boundary = cut_small + 1


