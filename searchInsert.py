class Solution(object):
    def searchInsert(self, nums, target):
        j = 0
        length = len(nums)
        while(j<length):
            if(nums[j]<target):
                j += 1
            else:
                return j
        return j