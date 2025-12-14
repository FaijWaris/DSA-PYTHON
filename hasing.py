#HASING BASIC
#storing frequency in dictinary
num=[4,2,3,4,5,6,7,8,1,1]
# freq=dict()
# for i in range(0,len(num)):
#     if num[i] in freq:
#         freq[num[i]]+=1
#     else:
#         freq[num[i]]=1    
# print(freq)

hash-map={}
n=len(num)
for i in range (0,n):
    hash-map[num[i]]=hash-map.get(num[i])+1
    