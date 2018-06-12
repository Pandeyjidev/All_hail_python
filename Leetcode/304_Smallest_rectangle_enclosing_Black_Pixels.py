# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

# For example, given the following image:

# [
#   "0010",
#   "0110",
#   "0100"
# ]
# and x = 0, y = 2,
# Return 6.

def check_list(lst):
    return '1' in lst

def get_index(lst):
    for i,r in enumerate(lst):
        if check_list(r):
            print("\n")
            return i
    return 0
def print_list(lst):
    print("\n")
    for i in lst:
        print ( ''.join(str(e) for e in i))
    print("\n")



x = ["10010",
     "11100",
     "11100"
]
rows = [list(i) for i in x]
lx = get_index(rows)

columns = [list(i) for i in zip(*x)]
ly = get_index(columns)

ref_row = [e[::-1] for e in rows[::-1]]
print_list(ref_row)
mx = len(ref_row) - get_index(ref_row) -1

ref_column = [ e[::-1] for e in columns[::-1]]
my = len(ref_column) - get_index(ref_column) -1

# print(mx)
# print(my)
print( (mx-lx+1) * (my-ly+1))