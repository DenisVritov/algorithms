"""
Implement a trie with insert, search, and startsWith methods.

Notes:
    You may assume that all inputs consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.

Example:

Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
"""

from typing import *


class Trie:

    class TrieNode:
        def __init__(self, value):
            self.val = value
            self.terminal = False
            self.children = dict()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = self.TrieNode(c)
            current_node = current_node.children[c]
        current_node.terminal = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return current_node.terminal

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return True
