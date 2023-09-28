# linear search
list = [42,25,78,65,35,56,70,26]
value = 65
for i in range(len(list)):
    if list[i] == value:
        print("Linear Search: ",value," found at index ",i)
        break
else:
    print("Linear Search: ",value," not found in the list")



#binary search 
list1 = [16,34,39,48,52,60,71,85]
value1 = 34
left, right = 0, len(list1) - 1
while left <= right:
    mid = left + (right - left) // 2
    if list1[mid] == value1:
        print("Binary Search: ",value1," found at index ",mid)
        break
    elif list1[mid] < value1:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Binary Search: ",value1," not found in the list")
