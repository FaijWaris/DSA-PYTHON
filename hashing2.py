# n=[5,3,4,5,6,7,8,9,0,1,2]
# m=[10,34,5,6,7,45,67,10]
# for i in m:
#     count=0
#     for j in n:
#         if j==i:
#             count+=1
#     print(f"{i} : {count}")
#HASHING TECHNIQUE
# n=[5,3,4,5,6,7,8,9,0,1,2]
# m=[10,34,5,6,7,45,67,10]

# hash_list = [0] * 11   # indexes 0 to 10

# # Step 1: Build hash list using values of n
# for x in n:
#     hash_list[x] += 1

# # Step 2: Check m values using hash
# for x in m:
#     if x < len(hash_list):   # check if index exists
#         print(f"{x} : {hash_list[x]}")
#     else:
#         print(f"{x} : 0"), 1

#CHARACTER HASHING
string="abbccdeeefffggg"
q=["d","e","f","a","z"]
hash_char=[0]*26
for char in string:
    index=ord(char)-ord('a')
    hash_char[index]+=1
for char in q:
    index=ord(char)-ord('a')
    print(f"{char} : {hash_char[index]}")


