class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def push(self,val):
        return self.stack.append(val)
    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return self.size() == 0


def string_to_int(string):
    string = string.strip()
    string = ''.join(string.split())
    string = list(string)
    # print(eval(''.join(string)))
    # print(string)
    eval_string(''.join(string))

def eval_string(string):
    st = Stack()
    s = ''
    res = 0
    for c in string:
        # print(st.size())
        if ord(c)>47 and ord(c)<57:
            s +=c
        elif c == '+':
            st.push(s)
            st.push('+')
            s = ''
        elif (not ord(c)>47) and (not ord(c)<57) and (c != '+'):
            return "Invalid Format"
        else:
            while(not st.is_empty()):
                x = st.pop()
                print(x)
                if x != '+':
                    res += int(x)
    print(res)
    # for c in string:
    #     if ord(c)>47 and ord(c)<57:
            

    








# string_to_int("9+10")
string_to_int("9+10            ")
# string_to_int("9+10+11")
# string_to_int("    9  +  10      ")
# string_to_int(" 9        +  10-11")
# string_to_int("9+10-11 ")