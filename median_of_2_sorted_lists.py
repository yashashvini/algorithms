class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        if(len1==1 and len2 == 0):
            return nums1[0]
        elif(len2==1 and len1 == 0):
            return nums2[0]
        elif(len1 == 0 and len2 == 0):
            return 0
        odd = 1
        if((len1+len2)%2 == 0):
            odd = 0
        median = (len1+len2)/2
        op = []
        i = 0
        j = 0
        k = -1
        while(i<len1 and j<len2):
            if(nums1[i]>=nums2[j]):
                op = op + [nums2[j]]
                k = k + 1
                j = j + 1
            elif(nums1[i]<nums2[j]):
                op = op + [nums1[i]]
                k = k + 1
                i = i + 1
            if(k == median):
                if(not odd):
                    return (op[median -1]+op[median])/2.0
                else:
                    return op[median]
        while(i<len1):
            op = op + [nums1[i]]
            k = k + 1
            i = i + 1
            if(k == median):
                 if(not odd):
                     return (op[median -1]+op[median])/2.0
                 else:
                     return op[median]
        while(j<len2):
            op = op + [nums2[j]]
            k = k +1
            j = j + 1
            if(k == int(median)):
                  if(not odd):
                      return (op[median -1]+op[median])/2.0
                  else:
                      return op[median]