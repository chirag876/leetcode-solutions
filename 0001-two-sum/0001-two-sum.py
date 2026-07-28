class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Iterate through each element in the list
        for i in range(len(nums)):

            # Compare the current element with the remaining elements
            # to avoid checking the same pair twice
            for j in range(i + 1, len(nums)):

                # Check if the current pair adds up to the target
                if nums[i] + nums[j] == target:

                    # Return the indices of the matching pair
                    return i, j