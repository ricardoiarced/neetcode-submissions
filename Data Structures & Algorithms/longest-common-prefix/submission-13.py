class TrieNode:
    def __init__(self):
        self.child = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]
    
    def lcp(self, word: str, prefixLen: int) -> int:
        node = self.root
        for i in range(min(len(word), prefixLen)):
            if word[i] not in node.child:
                return i
            node = node.child[word[i]]
        return min(len(word), prefixLen)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        mini = 0
        for i in range(1, len(strs)):
            if len(strs[mini]) > len(strs[i]):
                mini = i
        
        trie = Trie()
        trie.insert(strs[mini])
        prefixLen = len(strs[mini])
        for i in range(len(strs)):
            prefixLen = trie.lcp(strs[i], prefixLen)
        return strs[mini][:prefixLen]