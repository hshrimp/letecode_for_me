#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-06-10 11:17
"""
"""460. LFU缓存
请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。它应该支持以下操作：get 和 put。

get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
put(key, value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，
使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除最久未使用的键。
「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

进阶：
你是否可以在 O(1) 时间复杂度内执行两项操作？

示例：

LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4"""


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.num2key = {}
        self.key2num = {}
        self.flag = 0
        self.min_count = 0

    def get(self, key: int) -> int:
        if key in self.dict:
            num = self.key2num.get(key)
            self.num2key[num].remove(key)
            if num == self.min_count and not self.num2key[num]:
                self.min_count += 1
            if num + 1 in self.num2key:
                self.num2key[num + 1].append(key)
            else:
                self.num2key[num + 1] = [key]
            self.key2num[key] = num + 1
            return self.dict.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            num = self.key2num.get(key)
            self.num2key[num].remove(key)
            if num == self.min_count and not self.num2key[num]:
                self.min_count += 1
            if num + 1 in self.num2key:
                self.num2key[num + 1].append(key)
            else:
                self.num2key[num + 1] = [key]
            self.key2num[key] = num + 1
        else:
            if self.flag < self.capacity:
                self.dict[key] = value
                self.key2num[key] = 1
                if 1 in self.num2key:
                    self.num2key[1].append(key)
                else:
                    self.num2key[1] = [key]
                self.flag += 1
                self.min_count = 1
            elif self.dict:
                old = self.num2key[self.min_count].pop(0)
                self.key2num.pop(old)
                self.key2num[key] = 1
                if 1 in self.num2key:
                    self.num2key[1].append(key)
                else:
                    self.num2key[1] = [key]
                self.min_count = 1
                self.dict.pop(old)
                self.dict[key] = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
