# @before-stub-for-debug-begin
from python3problem2 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
      
class Solution:

    ##python中的整数除法是'//'而不是'/'
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        dummy = ListNode()
        tmp = dummy
        shiwei = 0
        while head1 or head2:
            val1 = head1.val if head1 else 0
            val2 = head2.val if head2 else 0
            gewei = (val1 + val2 + shiwei) % 10
            shiwei = (val1 + val2 + shiwei) // 10
            tmp.next = ListNode(gewei)
            tmp = tmp.next
            if head1: head1 = head1.next
            if head2: head2 = head2.next
            
        # 处理最后的进位        
        if shiwei > 0: tmp.next = ListNode(shiwei)
        return dummy.next
       
            
            

# @lc code=end

