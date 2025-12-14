num = [5, 7, 8, 4, 1, 6, 9, 2]

def selectionsort(num):
    n = len(num)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if num[j] < num[min_index]:#if i change the the sign so it willm  do in decending order
                min_index = j
        num[i], num[min_index] = num[min_index], num[i]
    
    return num   # VERY IMPORTANT

print(selectionsort(num))
