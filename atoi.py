class Solution(object):
    def myAtoi(self, str):
        op = 0
        neg = 0
        i = 0
        length = len(str)
        while(i<length):
            if(str[i] == ' '):
                i = i + 1
            elif(str[i] == '+'):
                i = i + 1
                break
            elif(str[i] == '-'):
                neg = 1
                i = i + 1
                break
            else:
                break
        while(i<length):
            a = ord(str[i])
            if(a==32):
                i = i + 1
            if(a>=48 and a<=57):
                op = op*10 + (a-48)
                i = i + 1
            else:
                break
        if(op>=pow(2,31)):
            if(neg):
                op = pow(2,31)
            else:
                op = pow(2,31) - 1
        if(neg==1):
            op = 0 - op
        return op
