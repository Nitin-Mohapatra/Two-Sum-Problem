class Solution(object):
   def twoSum(self, nums, target):
      hashMap = {}
      for i, num in enumerate(nums):
         complement = target - num
         if complement in hashMap:
            return [hashMap[complement],i]
         hashMap[num] = i
   
s = Solution()
print(s.twoSum([3,2,0,4,0],6)) # [0,1]
