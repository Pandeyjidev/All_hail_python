#  https://docs.python.org/3.1/library/collections.html
import re
from collections import Counter

# Occurences of word
def word_counter(string):
    string = string.split(' ')
    cnt = Counter()
    for word in string:
        cnt[word]+=1
    print(cnt)

# Using regex and open()
def count_word():
    words = re.findall('\w+', open('Sample.txt').read().lower())
    print(Counter(words).most_common(10))
    


word_counter("This is a word counter that counts words or word maybe counter the word . make sense ?")
count_word()