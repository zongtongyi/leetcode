#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Node(object):
    def __init__(self):
        self.word = None
        self.children = {}

class WordDictionary(object):

    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.word = word

    def __search(self, word, node):
        if not word: return True if node.word else False

        c = word[0]
        if c == '.':
            for k, node in node.children.iteritems():
                if self.__search(word[1:], node): return True
        if c not in node.children: return False
        return self.__search(word[1:], node.children[c])

    def search(self, word):
        return self.__search(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
# wordDictionary.addWord("bad")
# wordDictionary.addWord("dad")
# wordDictionary.addWord("mad")
# print wordDictionary.search(".ad")
# print wordDictionary.search("d..")
# print wordDictionary.search("a")
wordDictionary.addWord("a")
wordDictionary.addWord("ab")
print wordDictionary.search("a")
print wordDictionary.search("a.")
print wordDictionary.search("ab")
print wordDictionary.search(".a")
print wordDictionary.search(".b")
print wordDictionary.search("ab.")
print wordDictionary.search(".")
print wordDictionary.search("..")
# [true,true,true,false,true,false,true,true]
