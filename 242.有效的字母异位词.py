#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 可以先判断一下长度是否相等，不相等则一定不是：
        if len(s) != len(t): return False
        # 字符串转List
        n = len(s)
        dic = {}
        for i in range(n):
            # hashmap用法:
            #判断是否存在:in
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
        m = len(t)
        for j in range(m):
            if t[j] not in dic:
                return False
            else:
                dic[t[j]] -= 1
        for value in dic.values():
            if value != 0:
                return False
        return True

# @lc code=end

