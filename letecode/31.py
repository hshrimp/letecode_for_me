#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-06 09:43
"""
"""实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                p = i
                break
        else:
            nums[:] = nums[::-1]
            return
        for i in range(len(nums) - 1, p, -1):
            if nums[i] > nums[p]:
                nums[i], nums[p] = nums[p], nums[i]
                nums[p + 1:] = nums[-1:p:-1]
                return


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextPermutation([1, 2, 3]))
