#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. 快慢指针找到中间点
        # 2. 反转后半部分链表
        # 3. 比较两链表是否相等
        headA = head
        headB = self.find_half(head)
        headB = self.reverse(headB)
        curA = headA
        curB = headB
        flag = True
        while curA != None and curB != None:
            if curA.val != curB.val:
                flag = False
                break
            curA = curA.next
            curB = curB.next
        return flag
    
    def find_half(self, head):
        slow, fast = head, head
        while fast and fast.next:  # 此条件确保当 fast 指针还有两个或以上的节点可以前进时，它才前进两步
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head):
        pre = None
        cur = head
        while cur != None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

# @lc code=end

