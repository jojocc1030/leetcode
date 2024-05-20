#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        dummy = ListNode()
        tmp = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                tmp.next = head1
                tmp = head1
                head1 = head1.next
            else:
                tmp.next = head2
                tmp = head2
                head2 = head2.next
        if head1 is None:
            tmp.next = head2
        else: tmp.next = head1
        return dummy.next

# @lc code=end

