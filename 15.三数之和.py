#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start

# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # 三元组顺序不重要
        # i< j < k
        # 什么时候会出现重复三元组？当前枚举的数和上一个数相等
        ans = []
        n = len(nums)
        for i in range(n - 2):
            x = nums[i]
            # 优化  
            if x + nums[i + 1] + nums[i + 2] > 0:
                break
            # 优化
            if x + nums[n -1] + nums[n - 2] < 0:
                continue
            if i > 0 and x == nums[i-1]:  # 不能有重复的三元组
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sum = x + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                elif sum < 0: 
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                

        return ans
# @lc code=end

