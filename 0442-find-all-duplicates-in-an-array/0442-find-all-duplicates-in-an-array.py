class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        duplicate = set()

        for i in nums:
            if i in seen:
                duplicate.add(i)
            else:
                seen.add(i)
        return list(duplicate)
        