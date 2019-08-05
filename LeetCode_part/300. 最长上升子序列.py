"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        res = 0
        length = len(nums)
        # dp状态集合：存储最长上升子序列长度
        dp = [0 for _ in range(length)]

        for i in range(1, length):
            for j in range(i):
                if nums[j] < nums[i]:
                    # 遍历j时，取最大的dp[i]
                    dp[i] = max(dp[i], dp[j])
            # + 1：加上dp[i]自己
            res = max(res, dp[i]) + 1

        return res
