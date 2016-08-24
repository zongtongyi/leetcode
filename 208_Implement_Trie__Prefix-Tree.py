#! /usr/bin/env python
# -*- coding:utf-8 -*-
#

class TrieNode(object):
    def __init__(self):
        self.word = None
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        if not node.word: return False

        return True

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]

        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print trie.search('app')
    print trie.startsWith('app')

