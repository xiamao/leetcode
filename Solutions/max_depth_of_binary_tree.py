#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/10 22:23
# @Author  : xiamao
# @File    : max_depth_of_binary_tree.py


class Solution(object):
    def max_depth(self, root):
        if not root:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1


if __name__ == '__main__':
    pass
