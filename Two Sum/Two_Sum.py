class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 直接做两层遍历并记录下标
        l = len(nums)
        answer = []
        for i in range(l):
            for j in range(i+1,l):
                if (nums[i]+nums[j] == target):
                    answer.extend([i,j])
        return answer

Success Details 
Runtime: 3750 ms, faster than 23.17% of Python online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 24.14% of Python online submissions for Two Sum.