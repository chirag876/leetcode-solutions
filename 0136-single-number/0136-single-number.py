class Solution(object):
    def singleNumber(self, nums):

        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] +=1
            else:
                freq[nums[i]] = 1

        for i in freq.keys():
            if freq[i] == 1:
                return i