class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) == 0:
            return True

        note_set = set(ransomNote)
        note_dict = {}
        for ch in note_set:
            note_dict[ch] = ransomNote.count(ch)
#        print(note_dict)
        flag = False
        for ch in note_dict:
            if ch in magazine and note_dict[ch] <= magazine.count(ch):
                flag = True
            else:
                return False
        return flag
                