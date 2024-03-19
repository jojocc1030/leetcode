#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#


# 滑动窗口
# 时间复杂度：O(n)
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        ans = 0
        left = 0
        res = 1

        for right, x in enumerate(nums):
            res *= x
            while res >= k :
              
                res = res / nums[left]
                left += 1
          
            ans += right - left + 1
        return ans
# @lc code=end

