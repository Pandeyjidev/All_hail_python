class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if not words1 and not words2:
            return True
        if len(words1) != len(words2):
            return False

        word_dict = {}
        for pair in pairs:
            if pair[0] not in word_dict:
                word_dict[pair[0]] = set([pair[1]])
            else:
                word_dict[pair[0]].add(pair[1])

        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            if words1[i] in word_dict:
                value_set = word_dict[words1[i]]
                if words2[i] in value_set:
                    continue
            if words2[i] in word_dict:
                value_set = word_dict[words2[i]]
                if words1[i] in value_set:
                    continue
            return False

        return True