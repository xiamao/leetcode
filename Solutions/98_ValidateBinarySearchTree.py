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
        return self.is_valid_helper(root, -2 ** 31 - 1, 2 ** 31 + 1)

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

    def recover_bst(self, root):
        node_list = []
        val_list = []
        self.inorder(root, node_list, val_list)
        val_list.sort()
        for i, node in enumerate(node_list):
            node.val = val_list[i]

    def inorder(self, root, n_list, v_list):
        if not root:
            return
        self.inorder(root.left, n_list, v_list)
        v_list.append(root.val)
        n_list.append(root)
        self.inorder(root.right, n_list, v_list)

    def inorder_stack(self, root):
        stack = []
        node = root
        while node and stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print node.val
            node = node.right

    def morris_traversal(self, root):
        """
        Morris Traversal   Threaded binary tree
        A binary tree is threaded by making all right child pointers that would normally be pull point to the inorder
        successor of the node(if it exists), and all left child pointers that would normally be null point to the inorder
        predecessor of the node.
        1、初始化指针cur 指向root
        2、当cur不为空时
            如果cur没有左子节点
                打印出cur的值
                将cur的指针指向其右子节点
            反之
              将pre指针指向cur的左子树中的最右子节点
                若pre不存在右子节点
                  将其右子节点指回cur
                  cur指向其左子节点
        """



if __name__ == '__main__':
    tree = TreeNode(2)
    tree.left = TreeNode(3)
    tree.right = TreeNode(1)
    so = Solution()
    # print so.isValidBST(tree)
    # print so.is_valid_bst_sec(tree)
    so.recover_bst(tree)
    print tree.left.val
