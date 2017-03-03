"""Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero."""
class Solution(object):
    def threeSum(self, nums):
        op = []
        length = len(nums)
        i = 0
        nums.sort()
        while (i < length - 2):
            if (i > 0 and nums[i] == nums[i - 1]):
                i = i + 1
                continue
            j = i + 1
            k = length - 1
            while (j < k):
                sum = nums[i] + nums[j] + nums[k]
                if (sum < 0):
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    op.append([nums[i], nums[j], nums[k]])
                    while (j < k and nums[j] == nums[j + 1]):
                        j += 1
                    while (j < k and nums[k] == nums[k - 1]):
                        k -= 1
                    j += 1
                    k -= 1
            i += 1
        return op
