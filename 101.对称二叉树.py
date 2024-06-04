#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 对称需要满足以下条件：
        # L.val = R.val ：即此两对称节点值相等。
        # L.left.val = R.right.val ：即 L 的 左子节点 和 R 的 右子节点 对称。
        # L.right.val = R.left.val ：即 L 的 右子节点 和 R 的 左子节点 对称。
        if not root:
           return True
        def isSym(L, R) -> bool:
          if not L and not R:
             return True
          if not L or not R or L.val != R.val:
             return False
          return isSym(L.left, R.right) and isSym(L.right, R.left)
        return isSym(root.left, root.right)  



# @lc code=end

