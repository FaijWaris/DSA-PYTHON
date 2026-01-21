def quick_sort(nums, low, high):
    if low >= high:
        return

    pivot = nums[(low + high) // 2]
    i, j = low, high

    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    quick_sort(nums, low, j)
    quick_sort(nums, i, high)


nums = [3, 6, 8, 10, 1, 2, 1]
quick_sort(nums, 0, len(nums) - 1)
print(nums)

