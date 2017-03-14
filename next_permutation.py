class Solution(object):
    def nextPermutation(self, nums):
        length = len(nums)
        i = length
        if(i==1):
            return
        while(i>0 and (nums[i-1] <= nums[i-2])):
            i -= 1
        i -= 1
        if(i!=0):
            l = length
            while(l>i and (nums[i-1] >= nums[l-1])):
                l -= 1
            temp = nums[i-1]
            nums[i-1] = nums[l - 1]
            nums[l - 1] = temp
            if(i+1 == length):
                return
            k = i+1
            while(k<length):
                j = k
                while(j>i and nums[j-1] > nums[j]):
                    temp = nums[j-1]
                    nums[j-1] = nums[j]
                    nums[j] = temp
                    j -= 1
                k += 1
            return
        nums.sort()
        return