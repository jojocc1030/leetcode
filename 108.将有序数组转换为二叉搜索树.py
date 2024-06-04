#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 二叉搜索树的中序遍历是升序序列, 因此本题等同于根据中序遍历恢复BTS
# 主要思路： 每次使用mid作为中间根节点，然后在mid左右子树中选出根节点，依次递归

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        lo = 0
        hi = len(nums) - 1
        def midSearch(lo, hi, nums) ->  Optional[TreeNode]:
            if lo > hi:
                return None
            mid = lo + (hi - lo) // 2
            root = TreeNode(nums[mid])
            root.left = midSearch(lo, mid - 1, nums)
            root.right = midSearch(mid + 1, hi, nums)
            return root
        
        return midSearch(lo, hi, nums)


# @lc code=end

