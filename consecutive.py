def maxones(nums):
    count = max_count = 0

    for num in nums:
        count = count + 1 if num == 1 else 0
        max_count = max(max_count, count)

    return max_count


nums = [1,1,2,3,1,1,1,1,4,5,1,1]
print(maxones(nums))


