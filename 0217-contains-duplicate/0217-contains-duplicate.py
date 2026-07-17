class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
    :type nums: List[int]
    :rtype: bool
    """
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] +=1
            else:
                freq[nums[i]] = 1
        for keys in freq.keys():
            if freq[keys] > 1:
                return True
        return False
    
        