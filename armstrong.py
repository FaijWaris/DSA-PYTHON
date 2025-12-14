n=153
num=ntotal=0
nod=len(str(n))
while num>0:
    ld=num%10
    total=total+(ld**nod)
    num=num//10
if total==n:
    print("its is amsstron num")
else:
    print("it is not")    