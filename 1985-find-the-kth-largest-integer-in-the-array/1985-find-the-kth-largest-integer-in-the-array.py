class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # Sort the numeric strings in descending order using their integer values.
        # 'key=int' ensures comparison is based on numeric value, not lexicographical order.
        nums.sort(key=int, reverse=True)

        # Since the list is sorted in descending order,
        # the kth largest element is at index (k - 1).
        return nums[k - 1]