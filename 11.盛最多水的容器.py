#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_w = min(height[left], height[right]) * (right - left)
        while left != right:
            cur_w = min(height[left], height[right]) * (right - left)
            max_w = max(cur_w, max_w)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return max_w
# @lc code=end

