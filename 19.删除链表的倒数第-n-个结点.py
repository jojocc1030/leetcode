#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #双指针问题，需要删除倒数第n个节点，需要找到倒数(n+1)个节点
        # dummy节点存在的必要性！！！！！！
        dummy = ListNode(next=head)
        fast,slow = dummy, dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        # 当前slow为倒数(n+1)节点
        slow.next = slow.next.next
        
        return dummy.next


# @lc code=end

