nums=[5,10,-3,-1,-10,6]
n=len(nums)
result=[0]*n
posIndex,negIndex=0,1
def rearangearray(n,result,posIndex,negIndex):
 for i in range(0,n):
   if nums[i]>=0:
     result[posIndex]=nums[i]
     posIndex+=2 
   else:
     result[negIndex]=nums[i]
     negIndex+=2
   return result  
    
print(rearangearray(n,result,posIndex,negIndex))    