# print("Hello")

# input as string
# to int
# 0 or more whitespace
#not int
# 2 ++ || No +

def string_to_int(string):
  string = string.strip()
  string = ''.join(string.split())
  string = list(string)
#   string = string.strip()
#   print(string)
  integer=''
  val1=''
  for c in range(len(string)):
#     print(string[c])
#     if odr(string[c])>47 and odr(string[c])<58:
    if ord(string[c])>47 and ord(string[c])<58:
      integer = integer+ str(c)
    elif string[c] == '+':
#       print()
      idx = string.index(c)
      val1 = string[idx+1:]
      print(val1)
      try: 
#         print(string.index(string(c)))
        idx = string.index(c)
        val1 = string[idx+1:]
        print(val1)
        return int(val1) + int(integer) 
      except:
        return "Invalid Format 1" 
    elif string[c] == ' ':
      val1 = int(integer)
      integer = ''
      pass
  return "Invalid Format 2"
      
print(string_to_int("9+10"))