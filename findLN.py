#find lage no.

num = [23, 34, 44, 56, 67, 99]

# def findlargestvalue(num):
#     largest = num[0]
#     for i in num:
#         if i > largest:
#             largest = i
#     return largest

# print(findlargestvalue(num))
#find 2nd largest value in array
def second_largest(num):
    largest = float('-inf')
    second_largest = float('-inf')

    for i in num:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i

    return second_largest

print(second_largest(num))