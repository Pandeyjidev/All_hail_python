class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence)+' '
        start,end = 0 , len(s)
        for i in range(rows):
            start +=cols
            if s[start%end] !=' ':
                start -=1
            start +=1
        return start/end
    
    