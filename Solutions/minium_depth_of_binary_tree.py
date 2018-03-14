#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/10 22:20
# @Author  : xiamao
# @File    : minium_depth_of_binary_tree.py
from leetcode_util.TreeNode import TreeNode


class Solution(object):
    def min_depth(self, root):
        if not root:
            return 0
        if not root.left:
            return self.min_depth(root.right) + 1
        if not root.right:
            return self.min_depth(root.left) + 1
        return min(self.min_depth(root.left), self.min_depth(root.right)) + 1

