class Solution(object):
    def fourSum(self, nums, target):
        op = []
        length = len(nums)
        n = 0
        nums.sort()
        while(n < length - 3):
            if(n > 0 and nums[n] == nums[n - 1]):
                n += 1
                continue
            i = n + 1
            while (i < length - 2):
                if (nums[i] == nums[i - 1] and (i-1)!=n):
                    i += 1
                    continue
                j = i + 1
                k = length - 1
                while (j < k):
                    sum = nums[n] + nums[i] + nums[j] + nums[k]
                    if (sum < target):
                        j += 1
                    elif sum > target:
                        k -= 1
                    else:
                        op.append([nums[n],nums[i], nums[j], nums[k]])
                        while (j < k and nums[j] == nums[j + 1]):
                            j += 1
                        while (j < k and nums[k] == nums[k - 1]):
                            k -= 1
                        j += 1
                        k -= 1
                i += 1
            n += 1
        return op