class Solution:
    def findMinDifference(self, tps):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def toint(s):
            h, m = s.split(':')
            return int(h)*60+int(m)
        
        arr = sorted(map(toint, tps))
        
        mini = sys.maxsize
        for i in range(len(arr)-1):
            mini = min(arr[i+1]-arr[i], mini)
            if mini==0:
                return 0
        
        mini = min(mini, 24*60-(arr[-1]-arr[0]))
        return mini