# aaabbccccd -> a3b2c4d1
def compress_string(string):
    n = len(string)
    count = 1
    res = ""
    for idx,c in enumerate(string):
        if idx+1<n and string[idx]==string[idx+1]:
            count +=1
        else:
            res = res + c + str(count)  
            count = 1  
    return res

#3[abc]2[a]5[d]
def expand_string(string):
    string = string.lower()
    n=len(string)
    temp = ""
    res = ""
    mux = None
    for idx,c in enumerate(string):
        if ord(c)>47 and ord(c)<58:
            mux = int(c)
        elif c == '[':
            temp = ""
            continue
        elif ord(c)>96 and ord(c)<123:
            temp +=c
        else:
            res = res + str(mux*temp)
    return res
print(compress_string("aaabbccccd"))
print(expand_string("3[abc]2[b]4[x]"))
