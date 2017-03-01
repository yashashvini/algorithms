class Solution(object):
    def isPalindrome(self, x):
        neg = False
        num = x
        if(x < 0):
            neg = True
            x = 0 - x
        op = 0
        while(x > 0):
            i = x % 10
            x = int(x/10)
            op = op*10 + i
        if(op > 2147483647):
            return False
        if(op == num):
            return True
        return False