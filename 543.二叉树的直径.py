#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 1. 最长路径 = 经历的最多节点数 - 1
# 2. 最多节点数 = L + R + 1


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 1
        def depth(root):
            if not root:
                return 0
            L = depth(root.left)
            R = depth(root.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1
        depth(root)
        return self.ans - 1
        
# @lc code=end

