#1. WAP to perform following operation a string:   1. find the length     2. lowercase the string    3. uppercase the string    
# 4. slicing method    5. find the index of character from the string      6. count a character’s occurrence
str = "I'm from Miet"
length = len(str)
print("1. Length of the string:", length)
lowercase_string = str.lower()
print("2. Lowercase string:", lowercase_string)
uppercase_string = str.upper()
print("3. Uppercase string:", uppercase_string)
sliced_string = str[2:8]
print("4. Sliced string:", sliced_string)
char_to_find = "r"
char_index = str.index(char_to_find)
print("5. Index of 'r' in the string:", char_index)
char_to_count = "m"
char_count = str.count(char_to_count)
print("6. Occurrence of 'm' in the string:", char_count)




#2. WAP to swap two numbers by using bitwise without 3rd operator
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Original numbers: num1 =", num1, "num2 =", num2)
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2
print("Swapped numbers: num1 =", num1, "num2 =", num2)





#3. WAP toggle the Kth bit by using bitwise operator
num = int(input("Enter a number: "))
k = int(input("Enter the position (K) of the bit to toggle: "))
print("Original number:", num)
mask = 1 << k+1
result = num ^ mask
print("The", k, "th bit has been toggled. Result:", result)







#4. WAP to unset the rightmost set bit by bit manipulation
a=int(input("Enter the number : "))
a=a&(a-1)
print("The number after unsetting the rightmost set bit", a)



#5. WAP to convert lowercase character to uppercase using bit opertaor
char = input('Enter a lower case letter: ')
a=ord(char)
a=a&(~(1<<5))
print(chr(a))




#6. Write a program to find area parameter of circle square and rectangle by user choice
def circle():
    r=int(input("Enter radius of Circle :"))
    area=3.14*r*r
    Parameter=2*3.14*r
    print("Area of circle with radius,",r,":",area,"\n")
    print("Parameter of circle with radius,",r,":",Parameter,"\n")
def square():
    side=int(input("Enter length of Side for Square :"))
    area=side**2
    perimeter=4*side
    print("Area of Square with side,",side,":",area,"\n")
    print("Parameter of Square with side,",side,":",perimeter,"\n")
def rectangle():
    l=int(input("Enter Length of Rectangle :"))
    b=int(input("Enter Breadth of Rectangle :"))
    area=l*b
    perimeter=(2*(l+b))
    print("Area of Rectangle with length,",l,"and breadth,",b,":",area,"\n")
    print("Parameter of Rectangle with length,",l,"and breadth,",b,":",perimeter,"\n")
while True:
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle ")
    print("4. Exit \n")
    ch=int(input("Enter Your choice : "))
    if ch==1:
        circle()
    elif ch==2:
        square()
    elif ch==3:
        rectangle()
    elif ch==4:
        break
    else:
        print("Invalid Choice")




#7.Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of country stamps. Find the total number of distinct country stamps?
n=int(input("Enter The Total number of country stamps : "))
country_stamp=set()
for i in range(0,n):
    country_name=input("Enter the  country stamp Name : ")
    country_stamp.add(country_name)
print("Total Number Of Distinct Country Stamps : ",len(country_stamp))





#8. Given a list, the task is to write a Python Program to find the Index containing String?
list=['Rakshit',75,50,'Gupta','Py',69,88,'Miet']
for i,item in enumerate(list):
    if isinstance(item, str):
        print(i,end=" ")



"""
9. wap to print the following pattern
    * * *
    * * *
    * * *
    * * *
"""
row=4
col=3
for i in range(row):
    for j in range(col):
        print("*", end=" ")
    print()

