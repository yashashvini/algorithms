class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        open = ['(','{','[']
        for each in s:
            if each in open:
                stack.append(each)
            else:
                if(len(stack)==0):
                    return False
                if ((each == ')' and stack[-1] == '(') or (each == ']' and stack[-1] == '[') or (each == '}' and stack[-1] == '{')):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False