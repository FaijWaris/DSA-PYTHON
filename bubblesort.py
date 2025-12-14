num=[5,3,4,6,7,8,9]
n=len(num)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
print(num)