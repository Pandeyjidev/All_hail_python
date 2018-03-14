def string_to_int(string):
    string = string.strip()
    string = ''.join(string.split())
    string = list(string)
    return eval_string(''.join(string))
# Eval string is evalutating t
def eval_string(string):
    res = 0
    string.replace(' ','')
    new_string = string.split('+')
    for c in new_string:
        try:
            curr_num = int(c)
            res += curr_num
        except:
            return "Invalid Input"
    return res

# Test Cases
print(string_to_int("9+10"))
print(string_to_int("9+10      -      "))
print(string_to_int("9+10+11"))
print(string_to_int("    9  +  10      "))
print(string_to_int(" 9        +  10-11"))
print(string_to_int("9+10-11 "))
print(string_to_int("9+10+       11           + 21"))
print(string_to_int("9+10-11 ="))
print(string_to_int("   &  9+10-11 "))
print(string_to_int("        #@ 9+10-11 "))
print(string_to_int("    9++10 11  "))
print(string_to_int("112.00 + 11 "))
print(string_to_int("-10 + 11 "))
print(string_to_int("-10 + -11"))
print(string_to_int("10%11 "))
print(string_to_int("  -9      +   1  0+           -11 "))