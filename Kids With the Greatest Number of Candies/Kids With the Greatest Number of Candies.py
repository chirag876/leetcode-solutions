class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        list1 = []
        c1 = max(candies)
        for i in range(0, len(candies)):
            list2 = candies[i] + extraCandies >=c1
            list1.append(list2)
        return list1
