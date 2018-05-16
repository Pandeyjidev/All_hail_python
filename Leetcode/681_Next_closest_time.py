class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = sorted(list([d for d in time if d.isdigit()]))
        minn = min(digits)
        
        for d in digits:
            if d > time[4] and d<="9":
                return time[:4] + d
            
        for d in digits:
            if d > time[3] and d<="5":
                return time[:3] + d + minn
            
        for d in digits:
            if d > time[1] and int(time[0]+d)<24:
                return time[:1] + d + ':' + minn * 2
            
        for d in digits:
            if d > time[0] and int(d+time[1])<24:
                return d + minn + ':' + minn * 2
        
        return minn * 2 + ':' + minn * 2