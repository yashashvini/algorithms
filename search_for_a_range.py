class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        low = 0
        high = length - 1
        while (low <= high):
            mid = int((low + high) / 2)
            if (nums[mid] == target):
                i = mid
                j = mid
                while (i - 1 >= 0 and nums[i - 1] == target):
                    i -= 1
                while (j + 1 < length and nums[j + 1] == target):
                    j += 1
                return [i, j]
            elif (nums[mid] > target):
                high = mid - 1
            elif (nums[mid] < target):
                low = mid + 1
        return [-1, -1]
