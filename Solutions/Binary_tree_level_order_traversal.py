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
                node_queue.pop(0)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            res.append(level_list)
        return res

    def levelOrderzag(self, root):
        res = []
        if not root:
            return []
        node = root
        node_queue = [node]
        flag = [0]
        while node_queue:
            level_queue = node_queue[:]
            level_list = []
            while level_queue:
                # print len(level_queue)
                node = level_queue.pop(0)
                if flag[0] == 0:
                    level_list.append(node.val)
                else:
                    level_list.insert(0, node.val)
                node_queue.pop(0)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            if flag[0] == 0:
                flag[0] = 1
            else:
                flag[0] = 0
            res.append(level_list)
        return res


if __name__ == '__main__':
    tree = TreeNode(2)
    tree.left = TreeNode(3)
    tree.right = TreeNode(1)
    so = Solution()
    print so.levelOrderzag(tree)
