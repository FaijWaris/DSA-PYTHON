# def func(x,n):
#     if n==0:
#         return 
#     print(x)
#     func(x,n-1)

# func("faij",5)  

def func(i,n):
    if i>n:
        return
    func(i+1,n)
    print(i) 
    

func(1,5)      