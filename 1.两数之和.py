#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = dict()

        for i, n in enumerate(nums):
            if target - n in hashtable:
                return [i, hashtable[target - n]]
            hashtable[n] = i
        return []

        
# @lc code=end

