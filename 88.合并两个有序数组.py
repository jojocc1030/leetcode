#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sort = []
        p, q = 0, 0
        while p < m or q < n:
            if p == m:
                sort.append(nums2[q:])
                break
            elif q == n:
                sort.append(nums1[p:])
                break
            elif  nums1[p] == nums2[q]:
                sort.append(nums1[p])
                sort.append(nums2[q])
                p += 1
                q += 1
            elif nums1[p] > nums2[q]:
                sort.append(nums1[p])
                p += 1
            elif nums2[q] > nums1[p]:
                sort.append(nums2[q])
                q += 1
        nums1[:] = sort

        
# @lc code=end

