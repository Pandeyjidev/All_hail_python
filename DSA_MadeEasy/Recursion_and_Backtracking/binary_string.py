lst = [1,2,3,4,5,6]
def binary(n):
    print("\n")
    print(lst)
    if n<1:
        print(lst)
    else:
        lst[n-1]=0
        binary(n-1)
        lst[n-1]=1
        binary(n-1)

binary(5)