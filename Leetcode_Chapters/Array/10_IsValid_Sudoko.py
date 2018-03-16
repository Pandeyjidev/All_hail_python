class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check rows
        for i in board:
            i = self.filter_dot(i)
            if(not self.has_duplicate(i)):
                return False
            
        # Create Columns     
        col = zip(*board)
        
        # Check Columns
        for i in col:
            i=self.filter_dot(i)
            if(not self.has_duplicate(i)):
                return False
        # Check Boxes    
        if self.check_around(1,1,board) and self.check_around(4,1,board) and self.check_around(7,1,board) and self.check_around(1,4,board) and self.check_around(4,4,board) and self.check_around(7,4,board) and self.check_around(1,7,board) and self.check_around(4,7,board) and self.check_around(7,7,board):
            return True
        else:
            return False


    # Check for Dupulicates    
    def has_duplicate(self,arr):
        a=set(arr)
        return len(arr)==len(a)
    
    # Check for the Boxes in Sudoku
    def check_around(self,i,j,board):
        lst = [board[i-1][j-1],board[i-1][j],board[i-1][j+1],board[i][j-1],board[i][j],board[i][j+1],board[i+1][j-1],board[i+1][j],board[i+1][j+1]]
        lst = self.filter_dot(lst)
        return self.has_duplicate(lst)
        
    # Remove all Occurences of '.'
    def filter_dot(self,lst):
        return list(filter(('.').__ne__,lst))