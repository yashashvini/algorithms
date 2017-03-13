#Given an array and a value, remove all instances of that value in place and return the new length.
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        j = 0
        length = len(nums)
        if(length == 1):
            if(nums[i] == val):
                return 0
            else:
                return 1
        while(j<length):
            if(nums[j] == val):
                j += 1
                while(j< length and (nums[j] == val)):
                    j += 1
                if(j == length):
                    return i
                nums[i] = nums[j]
                i += 1
                j += 1
            elif(i<j):
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                i+= 1
                j += 1
        return i