def productExceptSelf(self, nums):
      result = []

      for i in range(len(nums)):
          product = 1 
          for j in range(len(nums)):
              if i !=j:
                  product *=nums[j]
          result.append(product)
      return result
print(productExceptSelf([1,2,3,4]))