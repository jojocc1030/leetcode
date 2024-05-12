#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 冒泡排序思想，时间复杂度O(n^2)
        n = len(nums)
        for i in range (0, n):
            flag = True
            for j in range(0, n - i - 1):
                if nums[j] == 0:
                    nums[j] = nums[j+1]
                    nums[j+1] = 0
                    flag = False
            if flag:
                break
    
    def solotion_1(self, nums: List[int]) -> None:
        # 利用快排pivot的思想，使用0作为pivot每次交换使得非零在左侧，0在右侧
        # 时间复杂度O(n)，一次遍历双指针即可
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0: # 只要不等0就把nums[i]和nums[j]进行交换，会出现i,j相等在原位换的情况
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] =tmp
                j += 1



        
        
            
                     

           


# @lc code=end

