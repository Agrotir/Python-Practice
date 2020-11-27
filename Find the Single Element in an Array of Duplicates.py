# Given an array of integers, arr, where all numbers occur twice except one number which
# occurs once, find the number.

class Solution(object):
    def findSingle(self, nums):
        items = {}
        for i in nums:
            if i in items:
                items[i] += 1
            else:
                items[i] = 1
        for i in items:
            if items.get(i) == 1:
                return i


nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
