n=5873
num=n
count=0
while num >0:
    count+=1
    num=num//10
print("Number of digits:", count)
#same count doing with log logic
# from math import *
# def countdigits(num):
#     return int(log10(num))+1