#Reverse digits of an integer.
#The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
class Solution(object):
    def reverse(self, x):
        neg = False
        if(x < 0):
            neg = True
            x = 0 - x
        op = 0
        while(x > 0):
            i = x % 10
            x = x/10
            op = op*10 + i
        if(op > 2147483647):
            return 0
        if(neg):
            op = 0 - op
        return op