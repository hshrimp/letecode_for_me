#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/20 下午6:12
"""
"""211. 添加与搜索单词 - 数据结构设计
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
说明:

你可以假设所有单词都是由小写字母 a-z 组成的。"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.words = set()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words.add(word)
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur.get(char)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        li = set()
        for i, char in enumerate(word):
            if char != '.':
                li.add(i)
        length = len(word)
        for w in self.words:
            if len(w) == length:
                for i in li:
                    if w[i] != word[i]:
                        break
                else:
                    return True
        return False


from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.next = defaultdict(TrieNode)
        self.end = False


class WordDictionary2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.trie
        for char in word:
            cur = cur.next[char]
        cur.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.find(self.trie, word)

    def find(self, cur, word):
        if len(word) == 1:
            if word == '.':
                for c in cur.next:
                    if cur.next[c].end:
                        return True
                else:
                    return False
            else:
                if word in cur.next and cur.next[word].end:
                    return True
                else:
                    return False

        if word[0] == '.':
            for c in cur.next:
                if self.find(cur.next[c], word[1:]):
                    return True
            else:
                return False
        else:
            if word[0] in cur.next and self.find(cur.next[word[0]], word[1:]):
                return True
            else:
                return False


class WordDictionary3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = defaultdict(list)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie[len(word)].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(self.trie[len(word)], word)

    def _search(self, li, word):
        if li and not li[0] and not word:
            return True
        if not li[0] and word:
            return False
        if not li and not word:
            return False
        temp = []
        for i in li:
            if i[0] == word[0] or word[0] == '.':
                temp.append(i[1:])
        return self._search(temp, word[1:])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
