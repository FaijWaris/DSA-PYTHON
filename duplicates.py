num = [1,1,1,2,3,4,4,7,9,9,9,10]

n = len(num)
if n == 0:
    print(0)

i = 0  # slow pointer
for j in range(1, n):  # fast pointer
    if num[j] != num[i]:  # when we find a new unique number
        i += 1
        num[i] = num[j]

print("Number of unique elements:", i + 1)
print("Array after removing duplicates:", num[:i+1])
