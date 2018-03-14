class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        m = n // 2 # number of subproblems
        
        for i in range(m):
            tl = [i,i]
            tr = [i, n-(i+1)]
            br = [n-(i+1), n-(i+1)]
            bl = [n-(i+1), i]
            
            nSwaps = n-2*i-1
            k = 0
            while k < nSwaps:
                tl_num = matrix[tl[0]][tl[1]+k]
                tr_num = matrix[tr[0]+k][tr[1]]
                br_num = matrix[br[0]][br[1]-k]
                bl_num = matrix[bl[0]-k][bl[1]]
                
                matrix[tl[0]][tl[1]+k] = bl_num
                matrix[tr[0]+k][tr[1]] = tl_num
                matrix[br[0]][br[1]-k] = tr_num
                matrix[bl[0]-k][bl[1]] = br_num
                
                k += 1

arr =[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
cl = Solution()
cl.rotate(arr)