#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# 滑动窗口 + 哈希表

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        cnt = Counter() # hashmap key: char value: int
        for right, x in enumerate(s):
            cnt[x] += 1
            while cnt[x] > 1: # 固定右端点
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1) 
            

        return ans
# @lc code=end

