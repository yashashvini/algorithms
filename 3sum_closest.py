"""Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution."""
class Solution(object):
    def threeSumClosest(self, nums, target):
        length = len(nums)
        i = 0
        nums.sort()
        op = nums[0] + nums[1] + nums[2]
        while(i < length - 2):
            if(i > 0 and nums[i] == nums[i-1]):
                i = i + 1
                continue
            j = i + 1
            k = length - 1
            while(j < k):
                sum = nums[i] + nums[j] + nums[k]
                if (target - sum == 0):
                    return target
                elif((target - sum)> 0):
                    if(abs(target - sum) < abs(target - op)):
                        op = sum
                    j += 1
                elif ((target - sum) < 0):
                    if(abs(target - sum) < abs(target - op)):
                        op = sum
                    k -= 1
            i += 1
        return op