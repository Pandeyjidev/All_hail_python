class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def calculate_rows():
            for i in range(len(grid)):
                e = 0
                position_stack = []
                for j in range(len(grid[0])):
                    if grid[i][j] == 'W':
                        while position_stack:
                            pos = position_stack.pop()
                            grid[i][pos] = e
                        e = 0
                    elif grid[i][j] == 'E':
                        e +=1
                    else:
                        position_stack.append(j)
                while position_stack:
                    pos = position_stack.pop()
                    grid[i][pos] = e
        def calculate_columns():            
            for j in range(len(grid[0])):
                position_stack = []
                e = 0
                for i in range(len(grid)):
                    if grid[i][j] == 'W':
                        while position_stack:
                            pos = position_stack.pop()
                            grid[pos][j] +=e
                            max_val[0] = max(max_val[0],grid[pos][j])
                        e=0
                    elif grid[i][j] == 'E':
                        e +=1
                    else:
                        position_stack.append(i)
                while position_stack:
                    pos = position_stack.pop()
                    grid[pos][j] +=e
                    max_val[0] = max(max_val[0],grid[pos][j])
        if len(grid) == 0:
            return 0
        max_val = [0]
        calculate_rows()
        calculate_columns()
        return max_val[0]
        