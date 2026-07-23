class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Slice nums1 up to m, add nums2, sort them, and modify nums1 in-place
        nums1[:] = sorted(nums1[:m] + nums2[:n])
        return nums1