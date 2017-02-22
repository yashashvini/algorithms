#convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution(object):
    def convert(self, s, numRows):
        op = []
        for i in range(numRows):
            op.append([])
        i = 0
        j = 0
        length = len(s)
        while(i<length):
            while(j<numRows):
                if(i<length):
                    op[j].append(s[i])
                    j = j + 1
                    i = i + 1
                else:
                    break
            j = 0
            for x in range(numRows - 1, 1 , -1):
                if(i<length):
                    op[x-1].append(s[i])
                    i = i + 1
                else:
                    break
        res = ""
        for each in op:
            for i in each:
                 res = res + i
        return res