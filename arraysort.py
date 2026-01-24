num = [3, 5, 6, 7, 8, 9]

if all(num[i] <= num[i+1] for i in range(len(num)-1)):
    print("Array is sorted")
