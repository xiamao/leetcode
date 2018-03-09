#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 9:41
# @Author  : xiamao
# @File    : 96_UniqueSearchTrees.py


class Solution(object):
    def numTrees(self, n):
        """
        :param n:
        :return: int
        """
        if n <= 0:
            return 0
        res = [0 for _ in range(n + 1)]
        res[0], res[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                res[i] += res[j] * res[i - j - 1]
        return res[n]


if __name__ == '__main__':
    so = Solution()
    print so.numTrees(3)
