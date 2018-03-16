#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 16:48
# @Author  : xiamao
# @File    : pathsumii.py


class Solution(object):

    def pathSum(self, root, sum):
        out = []
        res = []
        self.path_sum_helper(root, sum, out, res)
        return res

    def path_sum_helper(self, root, sum, out, res):
        if not root:
            return
        out.append(root.val)
        if sum == root.val and not root.left and not root.right:
            res.append(out)
        self.path_sum_helper(root.left, sum - root.val, out, res)
        self.path_sum_helper(root.right, sum - root.val, out, res)
        del out[-1]
