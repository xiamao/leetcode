#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/10 17:10
# @Author  : xiamao
# @File    : blance_binary_tree.py
from leetcode_util.TreeNode import TreeNode


class Solution(object):
    """
    可以转换成先求树的高度，直观的计算两个子树的高度差，我觉得效果并不好
    """
    def is_blanced(self, root):
        # return True if not root else self.is_blanced(root)
        if not root:
            return True
        if abs(self.count_tree_height(root.left) - self.count_tree_height(root.right)) > 1:
            return False
        return self.is_blanced(root.left) and self.is_blanced(root.right)

    def count_tree_height(self, root):
        """
        用来计算树的高度的函数，利用递归的方法。
        :param root:
        :return:
        """
        if not root:
            return 0
        return 1 + max(self.count_tree_height(root.left), self.count_tree_height(root.right))

    def sub_is_blanced(self, root):
        if root.left and root.right and root.left:
            pass

    def is_balance_2(self, root):
        return self.depth(root) != -1

    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1


if __name__ == '__main__':
    pass

