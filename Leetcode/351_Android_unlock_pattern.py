class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        boundaries = [m,n]
        odd_corners = [1,3,7,9]
        even_corners = [2,4,6,8]
        visited = [False]*9
        res = [0]
        def dfs(prev, steps):
            if boundaries[0] <= steps <= boundaries[1]:
                res[0] +=1
            if steps == boundaries[1]:
                return
            for next_val in range(1,10):
                if not visited[next_val-1]:
                    if prev in odd_corners and next_val in odd_corners and not visited[(prev+next_val)//2 -1]:
                        continue
                    elif prev in even_corners and next_val==10-prev and not visited[4]:
                        continue
                    visited[next_val-1] = True
                    dfs(next_val ,steps+1)
                    visited[next_val-1] = False
   

        for i in range(1,10):
            visited[i-1] = True
            dfs(i,1)
            visited = [False]*9
        return res[0]