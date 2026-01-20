def rearrange_array(nums):
    n = len(nums)
    result = [0] * n
    pos_index = 0
    neg_index = 1

    for num in nums:
        if num >= 0 and pos_index < n:
            result[pos_index] = num
            pos_index += 2
        elif num < 0 and neg_index < n:
            result[neg_index] = num
            neg_index += 2

    return result


nums = [5, 10, -3, -1, -10, 6]
print(rearrange_array(nums))
