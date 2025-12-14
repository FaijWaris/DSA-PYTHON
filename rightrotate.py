#by right rotate by k way
num = [3,4,5,6,7,8]
n = len(num)
k = 8

rotation = k % n

for _ in range(rotation):
    e = num.pop()
    num.insert(0, e)

print(num)
