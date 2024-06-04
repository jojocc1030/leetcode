#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归法
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res)
        return res
    def dfs(self, root, res) -> List[int]:
        if root is None:
            return
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
        


# @lc code=end

