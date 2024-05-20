#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1.先判断链表是否有环
        # 2. 再寻找入环点，直接记结论：fast和slow相遇后，fast = head，之后fast 和 slow都每次各走一步，最后就会在入环点相遇
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                res = head
                while res != slow:
                    res = res.next
                    slow = slow.next
                return res
        return None
  # 本题最大问题是对什么时候return的是None的判定，最简单的逻辑是，把return None写在最后，若找到正确入口则提前返回，就不用考虑的所有返回None的情况 
# @lc code=end

