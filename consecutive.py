def maxones(nums):
    count = max_count = 0

    for num in nums:
        if num == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

    return max_count

nums = [1,1,2,3,1,1,1,1,4,5,1,1]
print(maxones(nums))

