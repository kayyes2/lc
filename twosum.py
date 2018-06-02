# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        itemdict = {}
        i = 0
        for num in nums:
            # hint: remember to add this check before adding the item, otherwise target=6 will return [3,3]
            if target-num in itemdict:
                return [i, itemdict[target-num]]
            itemdict[num] = i
            i+=1
        return [-1, -1]
