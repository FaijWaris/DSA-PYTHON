nums=[-2,1,-3,4,-1,2,1,-5,4]
n=len(nums)
maxi=float("-inf")
def subarray(nums,maxi):
 total=0
 for i in range (0,n):
    total=total+nums[i]
    maxi=max(maxi,total)
    if total<0:
        total=0
 return maxi       
 
print(subarray(nums, maxi))
