class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(list)

class Solution(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.children['.'] = '.'

    def searchPrefix(self, prefix):
        node = self.root
        for i, c in enumerate(prefix):
            if '.' in node.children:
                return prefix[:i]
            if c not in node.children:
                break
            node = node.children[c]
        return prefix
            
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        for word in dict:
            self.insert(word)
        new_words = []
        for word in sentence.split():
            new_words.append(self.searchPrefix(word))
        return ' '.join(new_words)