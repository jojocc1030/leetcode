# @before-stub-for-debug-begin
from python3problem143 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
    
    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 若节点个数为偶数，则返回的中点为 n/2+1
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        head1 = head
        head2 = self.findMid(head)
        head2 = self.reverseList(head2)
        while True:
            if head1 == head2 or head1.next == head2 : break
            new_h1 = head1.next
            new_h2 = head2.next
            head1.next = head2
            head2.next = new_h1
            head1 = new_h1
            head2 = new_h2
           # if head1 == head2 or head1.next == head2 : break
        return None

# def printList(head):
#     cur = head
#     while cur:
#         print(cur.val)  
#         cur = cur.next

# if __name__ == "__main__":
#     nums = []
#     for num in nums:
#         node
#     head = Solution().reorderList(node1)
#     printList(head)



# @lc code=end

