#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-04-22 11:02
"""
"""127. 单词接龙
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。"""


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        def check(word1, word2):
            flag = 0
            for p, q in zip(word1, word2):
                if p != q:
                    if flag == 0:
                        flag += 1
                    else:
                        return False
            if flag == 1:
                return True
            return False

        def track(li):
            nonlocal max_len
            if max_len == dif:
                return
            if len(li) + 1 >= max_len:
                return
            if li[-1] == endWord:
                max_len = len(li) + 1
                return
            for w in d[li[-1]]:
                if w not in li:
                    track(li + [w])

        d = {}
        length = len(wordList)

        for i in range(length - 1):
            for j in range(i + 1, length):
                if check(wordList[i], wordList[j]):
                    if wordList[i] in d:
                        d[wordList[i]].add(wordList[j])
                    else:
                        d[wordList[i]] = set([wordList[j]])
                    if wordList[j] in d:
                        d[wordList[j]].add(wordList[i])
                    else:
                        d[wordList[j]] = set([wordList[i]])

        temp = set()
        for w in wordList:
            if check(beginWord, w):
                temp.add(w)
        max_len = len(wordList) + 2
        dif = 1
        for p, q in zip(beginWord, endWord):
            if p != q:
                dif += 1
        list(map(track, [[w] for w in temp]))
        return max_len if max_len < len(wordList) + 2 else 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList) -> int:

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

            # Since all words are of same length.
        L = len(beginWord)
        from collections import defaultdict

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # Queue for BFS
        queue = [(beginWord, 1)]
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0

    def ladderLength3(self, beginWord: str, endWord: str, wordList) -> int:

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

            # Since all words are of same length.
        L = len(beginWord)
        from collections import defaultdict

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(set)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i + 1:]].add(word)

        # Queue for BFS
        queue = [(beginWord, 1)]
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord}
        while queue:
            current_word, level = queue.pop(0)
            print(current_word, level)
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # Next states are all the words which share the same intermediate state.
                if endWord in all_combo_dict[intermediate_word]:
                    return level + 1
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0


if __name__ == '__main__':
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.ladderLength3(beginWord, endWord, wordList))
