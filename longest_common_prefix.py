#Write a function to find the longest common prefix string amongst an array of strings.
class Solution(object):
    def longestCommonPrefix(self, strs):
        length = len(strs)
        if(length == 0):
            return ""
        op = strs[0]
        i = 1
        while(i < length):
            if(op == "" or strs[i] == ""):
                return ""
            if(len(op)<len(strs[i])):
                len1 = len(op)
            else:
                len1 = len(strs[i])
            j = 0
            while(j<len1):
                if(strs[i][j] == op[j]):
                    j = j + 1
                else:
                    break
            op = op[:j]
            i = i + 1
        return op