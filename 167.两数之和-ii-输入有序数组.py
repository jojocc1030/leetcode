#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start

# 时间复杂度O(n)
# 空间复杂度O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        # 双指针
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                break
            if s > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]


# @lc code=end

