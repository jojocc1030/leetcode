#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
import collections



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        

        for s in strs:
            d[''.join(sorted(s))].append(s)
        


        return list(d.values())
# @lc code=end

