import numpy as np
class test_data():
    req = -1
    def __init__(self):
        global req 

        # while(1):
        #     if(req == 1):
        #         isUnique(self, input("Give the word you wanna check for Unique"))
        #     if(req == -1):
        #         break
    def isUnique(self,s):
        temp = []
        for c in s:
            if c in temp:
                return False
            else:
                temp.append(c)
        return True
    def isPermutation(self,s1,s2):
        s1 = list(s1)
        s2 = list(s2)
        for c in s1:
            s2.remove(c)
        if(len(s2)==0):
            return True
        else:
            return False
    def isReverse(self,s1,s2):
        return s1 == s2[:-1]
    def Urlify(self,s):
        return s.replace(" ","%20")
    def Swap(self,s1,s2):
        s2,s1 = s1,s2
        return s1,s2
    def Palindrome_permutation(self,s):
        set_data = set()
        for c in s:
            # set_data.update(c)
            # print(set_data)
            if (c in set_data):
                # print('{}  {}'.format(c,set_data))
                set_data.discard(c)
                # print(c)
            else:
                set_data.add(c)
        # print(set_data)
        return len(set_data)<=1
    def oneAway(self,s1,s2):
        if(abs(len(s1)-len(s2))>1):
            return False
        s1 = list(s1)
        s2 = list(s2)
        cnt = 0
        for c in s1:
            if(c in s2):
                s2.remove(c)
        print(s2)
        if(len(s2)<=1):
            return True
        else:
            return False          
    def string_compression(self,s):
        s = list(s)
        cnt = 1
        res = []
        for i in range(1,len(s)):
            print(s[i])
            if s[i] == s[i-1]:
                cnt +=1
            else:
                res.append(s[i-1])
                res.append(cnt)
                cnt=1
        res.append(s[i-1])
        res.append(cnt)
        cnt=1
        dat=''.join(str(e) for e in res)
        print(dat)
    def rotate_matrix_anticlockwise(self, arr):
        a = np.transpose(arr)        
        a = a[::-1]
        print(a)
    def rotate_matrix_clockwise(self, arr):
        a = arr[::-1]
        a = np.transpose(a)        
        print(a)
    def rotate_alt(self,arr):
        arr[::] = [[arr[len(arr)-j-1][i] for j in range(len(arr[0]))] for i in range(len(arr))]
        # matrix[::]=[[matrix[len(matrix)-j-1][i] for j in range(len(matrix[0]))] for i in range(len(matrix))]
        print(arr)
    def rotate_matrix_clockwise_ListComprehension(self,matrix):
        matrix[::]=[[matrix[len(matrix)-j-1][i] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    def rotate_left(self,s,count):
        s = s[count:len(s)+1] + s[:count]
        print(s)
    def rotate_right(self,s,count):
        s = s[len(s)-count:] + s[:len(s)-count]
        print(s)
dat = test_data()

if __name__ =='__main__':
    # print("Choose one of the function below")
    # print('{0}.{1}'.format("1","isUnique"))
    # req = input("Enter a number : ")
    data = test_data()
    # print(data.isUnique("hat"))
    # print(data.isPermutation("bat","tab"))
    # print(data.isReverse("bat","tab"))
    # print(data.Urlify("https://Data found"))
    # print(data.Swap("a","b"))
    # print(data.Palindrome_permutation("mamda"))
    # print(data.oneAway("pale","bake"))
    # print(data.string_compression("aaaabbssdeeewwaa"))
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    # print(data.rotate_matrix_anticlockwise(arr))
    # print(data.rotate_matrix_clockwise(arr))
    # print(data.rotate_alt(arr))
    # print(np.zeros((3,3)))
    print(data.rotate_left("abcdefgh",3))
    print(data.rotate_right("abcdefgh",3))
