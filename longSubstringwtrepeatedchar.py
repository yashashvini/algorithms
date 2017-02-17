#Given a string, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substring = []
        length = len(s)
        i = 0
        op = 0
        j = i
        while(i<length):
            if((length - i) < op):
                return op
            while((j<length) and (s[j] not in substring)):
                substring.append(s[j])
                j = j + 1
            op = max(op,len(substring))
            if(j>= length):
                return op
            k = substring.index(s[j])
            i = i + k + 1
            substring = substring[k+1:]
        return op