num=[71,2,3,4,5,6,7]
n=len(num)
temp=num[n-1]
for i in range(n-2,-1,-1):
    num[i+1]=num[i]
    num[0]=temp
print(num)