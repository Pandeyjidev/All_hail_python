"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {}
        for e in employees:
            d[e.id] = e
            
        res = 0
        stk = []
        stk.append(d[id])
        while stk:
            curr = stk.pop()
            if curr.importance:
                res +=curr.importance
                for sub in curr.subordinates:
                    stk.append(d[sub])
        return res
            