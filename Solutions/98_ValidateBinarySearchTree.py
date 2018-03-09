#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 17:03
# @Author  : xiamao
# @File    : 98_ValidateBinarySearchTree.py
from leetcode_util.TreeNode import TreeNode


class Solution(object):
    def isValidBST(self, root):
        """
        用来验证是否是搜索二叉树
        方法一，根据性质，左<根<右
        :param root:
        :return:
        """
        if not root:
            return True
        return self.is_valid_helper(root, -2**31 - 1, 2**31 + 1)

    def is_valid_helper(self, root, mn, mx):
        if not root:
            return True
        if root.val <= mn or root.val >= mx:
            return False
        return self.is_valid_helper(root.left, mn, root.val) and self.is_valid_helper(root.right, root.val, mx)

    def is_valid_bst_sec(self, root):
        """
        方法二，由于二叉搜索树的中序遍历是有序列表，因此可以先将树进行中序遍历到列表中。
        :param root:
        :return:
        """
        tree_list = []
        self.inno_tree(root, tree_list)
        print tree_list
        for i, node in enumerate(tree_list):
            if i == 0:
                continue
            if node < tree_list[i - 1]:
                return False
            return True

    def inno_tree(self, root, li):
        """
        利用递归进行中序遍历
        """
        if not root:
            return
        self.inno_tree(root.left, li)
        li.append(root.val)
        self.inno_tree(root.right, li)


if __name__ == '__main__':
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    so = Solution()
    print so.isValidBST(tree)
    print so.is_valid_bst_sec(tree)
