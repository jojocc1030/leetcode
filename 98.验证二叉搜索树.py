#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from cmath import inf


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       def helper(root, lower, upper) -> bool:
           if not root:
               return True
           x = root.val
           return lower < x < upper and helper(root.left, lower, x) and helper(root.right, x, upper)
       return helper(root, -inf, inf)
    
# @lc code=end

