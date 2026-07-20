class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # Sort the list in descending order based on the integer value of each string.
        # 'key=int' converts each string to an integer only for comparison during sorting.
        lst = sorted(nums, key=int, reverse=True)

        # Convert the 1-based position (k) to a 0-based index.
        index = k - 1

        # Return the kth largest number as a string.
        return lst[index]