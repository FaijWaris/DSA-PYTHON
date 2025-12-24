def missingNumber(nums):
    n = len(nums)
    for i in range(0, n+1):
        if i not in nums:
            return i

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))
