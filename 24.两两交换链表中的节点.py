# @before-stub-for-debug-begin
from python3problem24 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head #设置哨兵节点
        cur = dummy

        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = cur.next.next
            node3 = node2.next
            cur.next = node2 
            node2.next = node1
            node1.next = node3 #之前忽略了 需要让node1.next指向node3
            cur = node1 #最后更新cur为node1
        return dummy.next


            
# @lc code=end

