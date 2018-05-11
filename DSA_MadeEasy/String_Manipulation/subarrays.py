def list_subarrays(arr):
    n = len(arr)

    for i in range(0,n):
        for j in range(i,n):
            lst = []
            for k in range(i,j+1):
                lst.append(arr[k])
            print(lst)
            main_lst.append(lst)

arr = [1,2,3,4]
main_lst = []
list_subarrays(arr)
print(main_lst)