class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(n,path,left,right):
            if len(path) == 2*n:
                res.append(path)
                return
            if left<n:
                dfs(n,path+"(",left+1,right)
            if right<left:
                dfs(n,path+")",left,right+1)
        res = []
        dfs(n,"",0,0)
        print(res)
        return res