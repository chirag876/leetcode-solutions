class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        lst = sorted(nums, key=int, reverse=True)
        index = k-1
        return lst[index]
