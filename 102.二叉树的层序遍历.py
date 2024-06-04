#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            # 最重要的是对size的理解，在每一层遍历开始时，当前层的节点数量=队列长度 
            size = len(queue)
            while size > 0:
                node = queue.popleft()
                tmp.append(node.val)
                size -= 1
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res       
            
# @lc code=end

