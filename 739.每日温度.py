#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    # 暴力解法会超时
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)
        for i in range(n):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                j += 1
            if j == n :
                res.append(0)
            else:
                res.append(j - i)
        return res
 # @lc code=end

