nums = [5, 3, 9, 8, 1, 6, 4, 10, -100]
target = 4

def find_index(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1   # if target not found

result = find_index(nums, target)
print(result)
