class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        # Step 1: Store left products
        left = 1

        for i in range(n):
            result[i] = left
            left *= nums[i]

        # Step 2: Multiply by right products
        right = 1

        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result