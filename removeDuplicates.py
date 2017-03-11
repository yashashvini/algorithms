#Remove duplicates in sorted array and return length (inplace)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        length = len(nums)
        if(not length):
            return 0
        while(j < length):
            if(nums[i] == nums[j]):
                j += 1
            elif(j!=i+1):
                i+=1
                nums[i] = nums[j]
                j += 1
            else:
                i += 1
                j += 1
        return i + 1