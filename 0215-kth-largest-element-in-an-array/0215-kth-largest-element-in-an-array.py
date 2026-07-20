class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = sorted(nums, reverse=True)
        index = k-1
        return lst[index]