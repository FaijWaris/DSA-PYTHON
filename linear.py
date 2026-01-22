nums = [5, 3, 9, 8, 1, 6, 4, 10, -100]
target = 4

def find_index(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1

print(find_index(nums, target))
