#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/20 上午11:12
"""
"""208. 实现 Trie (前缀树)
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.words = set()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.words.add(word)
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur.get(char, {})

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.trie
        for char in prefix:
            if char not in cur:
                return False
            cur = cur.get(char)
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
