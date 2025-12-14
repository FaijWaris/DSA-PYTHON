# def func(sum,i,n):
#     if i>n:
#         print(sum)
#         return
#     func(sum+i,i+1,n)
#     # print(i)


# func(0,1,5)    
#FUNCTIONAL RECURSION
def func(n):
    if n==1:
        return 1
    return n+func(n-1)
    

print(func(100))