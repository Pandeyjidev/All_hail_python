
import re
from collections import Counter
def word_count(data):
    # Filter to only Alphanumeric values
    data = filter(None,re.sub('[^A-Za-z0-9 ]','',data))
    # Remove extra spaces and make it a list
    data = data.lower().strip().split()
    # Count all the words and make a dictionary
    c = Counter(data)
    res = []
    x = []
    # Copy dictionary values as sequence
    for d in data:        
        if d not in x:
            res.append([d,str(c[d])])
            x.append(d)
    new_res = []
    # Sort the dictionary values with respect to the count
    for idx,tuple_data in enumerate(res):
        # if the count is greater than the first value of the list then insert it to 0
        if new_res and int(new_res[0][1]) < int(tuple_data[1]):
            new_res.insert(0,tuple_data)
        # Else find the correct position and insert it in there
        elif new_res and int(tuple_data[1]) > int(new_res[-1][1]):
            j = -2
            while(int(tuple_data[1])>int(new_res[j][1])):
                print(new_res)
                j -=1
            new_res.insert(j+1,tuple_data)    
        # If first value then just append to the new list
        else:
            new_res.append(tuple_data)
    return new_res

document = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"

print(word_count(document))