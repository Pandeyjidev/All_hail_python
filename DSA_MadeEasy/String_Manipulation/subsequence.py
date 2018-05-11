# Python 3 code to generate all
# possible subsequences.
# Time Complexity O(n * 2 ^ n) 
import math
 
def printSubsequences(arr, n) :
 
    # Number of subsequences is (2**n -1)
    opsize = math.pow(2, n)
    print(opsize)
    # Run from counter 000..1 to 111..1
    for counter in range( 1, (int)(opsize)) :
        print("Counter = " + str(counter) + " ")
        for j in range(0, n) :
            print("j = " + str(j) + " ") 
            # Check if jth bit in the counter
            # is set If set then print jth 
            # element from arr[] 
            if (counter & (1<<j)) :
                print( arr[j], end =" ")
         
        print()
 
# Driver program
arr = [1, 2, 3, 4]
n = len(arr)
print( "All Non-empty Subsequences")
 
printSubsequences(arr, n)