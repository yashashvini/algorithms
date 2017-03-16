class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        length = len(nums)
        high = length - 1
        if(length == 1):
            if(nums[0] == target):
                return 0
            else:
                return -1
        while(low < high):
            mid = int((low + high)/2)
            if(nums[mid] > nums[high]):
                low = mid + 1
            elif(low + 1 == high):
                high -= 1
            else:
                high = mid
        rot = low
        low = 0
        high = length - 1
        while(low <= high):
            mid = int((low + high)/2)
            realmid = int((mid+rot)%length)
            if (nums[realmid] == target):
                return realmid
            elif (nums[realmid] > target):
                high = mid - 1
            elif (nums[realmid] < target):
                low = mid + 1
        return -1