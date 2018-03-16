#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 16:38
# @Author  : xiamao
# @File    : pathsum.py


class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        elif not root.left and not root.right and root.val == sum:
            return True
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
