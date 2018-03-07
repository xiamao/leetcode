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
    mem = {}

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
        for root_val in range(start, end + 1):
            left_tree = self.dfs(start, root_val - 1)
            right_tree = self.dfs(root_val + 1, end)
            for i in left_tree:
                for j in right_tree:
                    root = TreeNode(root_val)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res

    def generate_trees(self, n):
        """
        动态规划的方法，计算好固定序列后将其作为子树存储，如果下次遍历中，如果遇到这个子序列即子树时可以
        直接使用。
        :param n:
        :return:
        """
        l = [i for i in range(1, n + 1)]
        return self.gen_helper(l)
        pass

    def gen_helper(self, l):
        if len(l) == 0: return []
        key = ':'.join(list(map(lambda x: str(x), l)))
        if key in self.mem:
            return self.mem[key]
        res = []
        for i in range(len(l)):
            lhs = self.gen_helper(l[:i])
            rhs = self.gen_helper(l[i + 1:])
            if len(lhs) == 0 and len(rhs) == 0:
                res.append(TreeNode(l[i]))
            elif len(lhs) == 0:
                for j in rhs:
                    rnew = TreeNode(l[i])
                    rnew.right = j
                    res.append(rnew)
            elif len(rhs) == 0:
                for k in lhs:
                    lnew = TreeNode(l[i])
                    lnew.left = k
                    res.append(lnew)
            else:
                for j in lhs:
                    for k in rhs:
                        rnew = TreeNode(l[i])
                        rnew.left = j
                        rnew.right = k
                        res.append(rnew)
        self.mem[key] = res
        return res
