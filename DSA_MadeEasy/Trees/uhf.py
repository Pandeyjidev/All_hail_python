from collections import *
def word_count_engine(document):
  #document = document.strip('')
  document = document.lower()
  lst = []
  temp = ''
  for i in document:
    if (ord(i) > 96 and ord(i) < 123) or i == ' ':
      if i == ' ':
        lst.append(''.join(str(e) for e in temp))
        temp = ''
      else:
        temp = temp + i
  if not(temp == ''):
    lst.append(''.join(str(e) for e in temp))
  #print(lst)
  c = Counter(lst)
  lst2 = []
#   print(c.items())
  for key, value in sorted(c.iteritems(), key=lambda: (k,v): (v,k)):
    if key =='':
        continue
    if not lst2:
      lst2.append([key,value])
    elif value > lst2[0][1]:
      lst2.insert([key,value],0)
    else:
      x=0
      while(x < len(c) and x < len(lst2) and value <= lst2[x][1] ):
        x +=1
      lst2.insert([key,value],x)
    
  return lst2


data = "perfect , data data's just just!! perfect"
print(word_count_engine(data))
