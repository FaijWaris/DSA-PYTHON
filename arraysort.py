num=[3,5,6,7,8,9]
n=len(num)
for i in range (0,n-1):
    if num[i]>num[i+1]:
       break
else:
    print("Array is sorted")
    exit(0)   
    