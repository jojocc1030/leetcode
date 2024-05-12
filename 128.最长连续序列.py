#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start

# set集合巧用: 去重, in/not in 判定
# O(n) 方法：如果n-1在set中 则n一定作为n-1的中间的点被判定过，因此跳过n
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cur = num
                cur_len = 0

                while cur in nums_set:
                    cur_len += 1 
                    cur += 1
                max_len = max(cur_len, max_len)
        
        return max_len

# @lc code=end

