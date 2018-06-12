def convert(s, numRows):
        if numRows <= 1:
            return s
        
        strArray = ['' for r in range(numRows)]
        mult = currRow = i = 0
        # print(strArray)
        
        for i in range(len(s)):
            if currRow == numRows - 1:
                mult = -1
            elif currRow == 0:
                mult = 1
            print(currRow)
            print(mult)
            print(s[i])
            print("\n ")
            strArray[currRow] += s[i]
            currRow += mult
        
        return ''.join(strArray)


convert('PAYPALISHIRING',3)
print(convert('PAYPALISHIRING',4))  #PAHNAPLSIIGYIR