    ·····#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start

# 滑动窗口， 合理利用都是正数这一条件-->具有单调性！！！
# 固定右端点，移动左端点
# 时间复杂度： O(n)
# 空间复杂度： O(1)
# 双指针使用条件： 单调性 
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        sum = 0
        ans = n + 1
        for right, x in enumerate(nums):
            sum += x
            while sum >= target:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
        return ans if ans <= n else 0
# @lc code=end

 