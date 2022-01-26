# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 构造大顶堆
# 1. 找出最大元素
# 2. 从最大元素开始两边展开分组进行递归

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:nums.index(root.val)])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(root.val)+1:])
        return root

Success
Details 
Runtime: 258 ms, faster than 34.36% of Python online submissions for Maximum Binary Tree.
Memory Usage: 14.1 MB, less than 86.10% of Python online submissions for Maximum Binary Tree.