#Linear Search
def linear_search(list,value):
    for i in range(len(list)):
        if list[i]==value:
            print("Number is found at index ",i)
            break
    else:
        print("Number not found")

#Binary Search
def binary_searh(list,value):
    start=0
    end=len(list)-1
    while start<=end:
        mid=start+(end-start)//2
        if list[mid]== value:
            print("Number found at the index -",mid)
            break
        elif list[mid]<value:
            start=mid+1
        else:
            end=mid-1
    else:
        print('Number not found')

#Linear Search
l1=[23,39,45,12,36,69,3,9]
print("Given List is - ",l1)
number=int(input("Enter the number to find in the list : "))
linear_search(l1,number)

#Binary Search
l2=[10,18,23,45,52,88,98]
print("Given List is - ",l2)
number1=int(input("Enter the number to find in the list : "))
binary_searh(l2,number1)
