
def twoSum(nums,target):
    count = {}
    length = len(nums)
    for i in range(length):
        if str(nums[i]) in count:
            a = count[str(nums[i])]
            count[str(nums[i])] = [a,i]
        else:
            count[str(nums[i])] = i
    print(count)
    for i in range(length):
        diff = target - nums[i]
        if (diff == nums[i]):
            if type(count[str(diff)]) == list:
                return count[str(diff)]
        elif str(diff) in count:
            return [i,count[str(diff)]]

def main():
    op = twoSum([0,4,3,0],0)
    print(op)
if __name__ == "__main__":
    main()