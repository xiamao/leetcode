#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 22:31
# @Author  : xiamao
# @File    : Binary_tree_level_order_traversal.py

from leetcode_util.TreeNode import TreeNode


class Solution(object):
    def levelOrder(self, root):
        res = []
        if not root:
            return []
        node = root
        node_queue = [node]
        while node_queue:
            level_queue = node_queue[:]
            level_list = []
            while level_queue:
                print len(level_queue)
                node = level_queue.pop(0)
                level_list.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            res.append(level_list)
        return res


if __name__ == '__main__':
    tree = TreeNode(2)
    tree.left = TreeNode(3)
    tree.right = TreeNode(1)
    so = Solution()
    print so.levelOrder(tree)
