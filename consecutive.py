nums = [1,1,2,3,1,1,1,1,4,5,1,1]

def maxones(nums):
    count = 0
    max_count = 0
    
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            max_count = max(max_count, count)  # update here
        else:
            count = 0
    
    return max_count   # return AFTER loop

print(maxones(nums))
