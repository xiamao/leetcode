#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/10 15:02
# @Author  : xiamao
# @File    : construct_bt_pre_inorder.py
from leetcode_util.TreeNode import TreeNode


class Solution(object):
    """
    先序遍历为  1，2, 4, 5, 3, 6, 7
    中序遍历为  4，2，5，1，6，3，7
    规律为
    1、先序遍历的从左数第一个为整个树的根节点，
    2、中序遍历的根节点是左子树右子树的分割点
    3、看这个树的左子树依然满足这个规律。
    因此可以采用递归来做。
    """

    def buildTree(self, preorder, inorder):
        # root = TreeNode(preorder[0])
        pre_len = len(preorder)
        in_len = len(inorder)
        return self.build_sub_tree(preorder, 0, pre_len - 1, inorder, 0, in_len - 1)

    def build_sub_tree(self, pre, pre_start, pre_end, in_, in_start, in_end):
        if in_start > in_end or pre_start > pre_end:
            return None
        root_val = pre[pre_start]
        root_index = [0]
        for i in range(in_start, in_end + 1):
            if in_[i] == root_val:
                root_index[0] = i
                break
        len = root_index[0] - in_start
        root = TreeNode(root_val)
        root.left = self.build_sub_tree(pre, pre_start + 1, pre_start + len, in_, in_start, root_index[0] - 1)
        root.right = self.build_sub_tree(pre, pre_start + len + 1, pre_end, in_, root_index[0] + 1, in_end)
        return root

    def build_bt_in_post(self, inorder, postorder):
        post_len = len(postorder)
        in_len = len(inorder)
        return self.build_sub_tree_in_post(postorder, 0, post_len - 1, inorder, 0, in_len - 1)

    def build_sub_tree_in_post(self, post, post_start, post_end, in_, in_start, in_end):
        if in_start > in_end or post_start > post_end:
            return None
        root_val = post[post_end]
        print root_val
        root_index = [post_end]
        for i in range(in_start, in_end + 1):
            if in_[i] == root_val:
                root_index[0] = i
                break
        len = root_index[0] - in_start
        root = TreeNode(root_val)
        if root_val == 3:
            print post_start, post_start + len - 1, len, post_end - len, post_end - 1, root_index[0] + 1, in_end, root_index[0] - 1
        root.left = self.build_sub_tree_in_post(post, post_start, post_start + len - 1, in_, in_start, root_index[0] - 1)
        root.right = self.build_sub_tree_in_post(post, post_start+len, post_end - 1, in_, root_index[0] + 1, in_end)
        return root


if __name__ == '__main__':
    # pre_ = [1, 2, 4, 5, 3, 6, 7]
    # ino_ = [4, 2, 5, 1, 6, 3, 7]
    in_ = [9, 3, 15, 20, 7]
    post = [9, 15, 7, 20, 3]
    so = Solution()
    # print so.buildTree(pre_, ino_).right.val
    print so.build_bt_in_post(in_, post).right.right.val
