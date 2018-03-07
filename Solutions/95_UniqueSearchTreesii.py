#!/usr/bin/env python
# coding:utf8
__author__ = "xiamao"
__time__ = "2018 / 3 / 7 下午2:21"


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        用来枚举1-n的所有二叉搜索树
        :param n: int
        :return: list[TreeNode]
        """

        if n == 0:
            return []

    def dfs(self, start, end):
        if start > end:
            return [None]
        res = []
        for root_val in range(start, end+1):
            left_tree = self.dfs(start, root_val - 1)
            right_tree = self.dfs(root_val+1, end)
            for i in left_tree:
                for j in right_tree:
                    root = TreeNode(root_val)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
