class Solution(object):
    def moveZeroes(self, nums):
        write = 0

        # Step 1: Saare non-zero elements ko aage lao
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        # Step 2: Remaining positions ko zero se fill karo
        while write < len(nums):
            nums[write] = 0
            write += 1

        return nums

        