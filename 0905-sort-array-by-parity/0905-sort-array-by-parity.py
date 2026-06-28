class Solution(object):
    def sortArrayByParity(self, nums):
            odd = []
            even = []
            # Step 2: Separate odd and even numbers
            for num in nums:
                # Hint: Complete this condition
                if num%2 != 0:
                    odd.append(num)
                else:
                    even.append(num)
            # Step 3: Sort odd numbers in descending order
            odd.sort(reverse=True)
            # Step 4: Sort even numbers in ascending order
            even.sort()
            # Step 5: Return final result
            return even + odd