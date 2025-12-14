# num=20 #Brut Foirce  solution
# result=[]
# for i in range(1,num+1):
#     if num%i==0:
#         print(f"factor of {num}")
#     else:
#         print(f"Not a factor of {num}")    

#Better optimize solution
# num = 10
# result = []  # use a list to store factors

# for i in range(1, num // 2):  # include num//2 also
#     if num % i == 0:
#         result.append(i)   # store the factor

# # Optionally, num itself is also a factor
# result.append(num)

# print("Factors:", result)

#BEST OPTIMAL SOLUTION
num = 36
factors = []

# Loop only till sqrt(num)
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        factors.append(i)           # i is a factor
        if i != num // i:           # avoid duplicates for perfect squares
            factors.append(num // i)  # num//i is also a factor

# Sort the list of factors
factors.sort()

print("Factors of", num, "are:", factors)
