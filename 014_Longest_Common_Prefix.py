#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):

    class Trie(object):
        
        class Node(object):
            def __init__(self):
                self.word = None
                self.children = {}
                
        def __init__(self):
            self.root = Solution.Trie.Node()
    
        def insert(self, word):
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = Solution.Trie.Node()
                node = node.children[c]
            node.word = word
        
        def lcp_dfs(self):
            res = []
            node = self.root
            while len(node.children)==1 and not node.word:
                k = node.children.keys()[0]
                res.append(k)
                node = node.children[k]
            
            return ''.join(res)
            
    def longestCommonPrefix(self, strs):
        if '' in strs: return ''
        
        trie = Solution.Trie()
        [trie.insert(s) for s in strs]
        return trie.lcp_dfs()



if __name__ == "__main__":
    strs = ['abc', 'abca', 'ab']
    print Solution().longestCommonPrefix(strs)
    