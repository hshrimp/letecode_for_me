#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/12/25 上午11:23
"""
"""432. 全 O(1) 的数据结构
请你实现一个数据结构支持以下操作：

Inc(key) - 插入一个新的值为 1 的 key。或者使一个存在的 key 增加一，保证 key 不为空字符串。
Dec(key) - 如果这个 key 的值是 1，那么把他从数据结构中移除掉。否则使一个存在的 key 值减一。如果这个 key 不存在，这个函数不做任何事情。key 保证不为空字符串。
GetMaxKey() - 返回 key 中值最大的任意一个。如果没有元素存在，返回一个空字符串"" 。
GetMinKey() - 返回 key 中值最小的任意一个。如果没有元素存在，返回一个空字符串""。
 
挑战：

你能够以 O(1) 的时间复杂度实现所有操作吗？"""

from collections import defaultdict


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(int)

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.d[key] += 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.d:
            return
        self.d[key] -= 1
        if not self.d[key]:
            self.d.pop(key)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        key = ''
        m = -1
        for k, v in self.d.items():
            if v > m:
                m = v
                key = k
        return key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        key = ''
        m = float('inf')
        for k, v in self.d.items():
            if v < m:
                m = v
                key = k
        return key

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
