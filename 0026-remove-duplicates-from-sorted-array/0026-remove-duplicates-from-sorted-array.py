class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
    # as first element will always be unique so we need to check what is the next unique element and write will do the same thing
        write = 1 
        # we will start from the first index because the value at the 0th index will always be unique
        for read in range(write, len(nums)):
            # as the array is sorted the current and previous values should not be equal for them to be unique
            if nums[read] !=nums[read-1]:
            # we have to keep on updating the index so the array will be updated
                nums[write] = nums[read]
            # keep on increasing the counter to the next unique element
                write +=1
        return write 
            