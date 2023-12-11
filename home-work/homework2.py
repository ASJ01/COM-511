#1
if __name__ == '__main__':
    print("Hello, World!")
#2

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

# Check conditions and print the result
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

#3
# Read input from the user
a = int(input().strip())
b = int(input().strip())

print(a + b)
print(a - b)
print(a * b)


#4
# Read input from the user
a = int(input().strip())
b = int(input().strip())

# Perform integer division and print the result
print(a // b)

# Perform float division and print the result
print(a / b)

#5
# Read input from the user
n = int(input().strip())

# Print the square of each non-negative integer less than n
for i in range(n):
    print(i ** 2)

#6
def is_leap(year):
    # Check if the year is a leap year based on the conditions provided
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Read input from the user
year = int(input().strip())

# Call the function and print the result
result = is_leap(year)
print(result)


#7
def is_leap(year):
    # Check if the year is a leap year based on the conditions provided
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input())
print(is_leap(year))

#8
# Read input from the user
n = int(input().strip())

# Print the consecutive integers without spaces
for i in range(1, n + 1):
    print(i, end='')

# Alternatively, you can use the join method to concatenate the numbers into a single string:
# result = ''.join(str(i) for i in range(1, n + 1))
# print(result)

#9
if __name__ == '__main__':
    s = input()

    # Check if the string has any alphanumeric characters
    print(any(c.isalnum() for c in s))
    
    # Check if the string has any alphabetical characters
    print(any(c.isalpha() for c in s))
    
    # Check if the string has any digits
    print(any(c.isdigit() for c in s))
    
    # Check if the string has any lowercase characters
    print(any(c.islower() for c in s))
    
    # Check if the string has any uppercase characters
    print(any(c.isupper() for c in s))

#10
def print_hackerrank_logo(thickness):
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c +
               (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))

if __name__ == '__main__':
    thickness = int(input())
    print_hackerrank_logo(thickness)

#11

x, y, z, n = (int(input()) for _ in range(4))

# Generate all possible coordinates using list comprehensions
coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

# Filter out coordinates where the sum is not equal to n
result = [coord for coord in coordinates if sum(coord) != n]

# Print the result
print(result)


#12
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # Convert the input to a list and remove duplicates by converting to a set
    scores = list(set(arr))

    # Sort the list in descending order
    scores.sort(reverse=True)

    # Print the second element, which is the runner-up score
    print(scores[1])
#13
if __name__ == '__main__':
    n = int(input())
    students = []

    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade
    second_lowest_grade = sorted(set(score for name, score in students))[1]

    # Filter students with the second lowest grade and sort alphabetically
    result = sorted(name for name, score in students if score == second_lowest_grade)

    # Print each name on a new line
    for name in result:
        print(name)
#14
if __name__ == '__main__':
    n = int(input())
    student_dict = {}

    # Read the names and marks into a dictionary
    for _ in range(n):
        input_data = input().split()
        name, marks = input_data[0], list(map(float, input_data[1:]))
        student_dict[name] = marks

    # Read the query_name
    query_name = input()

    # Calculate the average marks for the specified student
    average_marks = sum(student_dict[query_name]) / len(student_dict[query_name])

    # Print the result with 2 decimal places
    print("{:.2f}".format(average_marks))
#15
if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        command, *args = input().split()

        if command == 'insert':
            i, e = map(int, args)
            my_list.insert(i, e)
        elif command == 'print':
            print(my_list)
        elif command == 'remove':
            e = int(args[0])
            my_list.remove(e)
        elif command == 'append':
            e = int(args[0])
            my_list.append(e)
        elif command == 'sort':
            my_list.sort()
        elif command == 'pop':
            my_list.pop()
        elif command == 'reverse':
            my_list.reverse()
#16
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    # Create a tuple
    my_tuple = tuple(integer_list)

    # Print the result of hash function
    result = hash(my_tuple)
    print(result)
#17
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        return Points(self.y * no.z - self.z * no.y, self.z * no.x - self.x * no.z, self.x * no.y - self.y * no.x)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))


#18
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real_part = self.real * no.real - self.imaginary * no.imaginary
        imag_part = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real_part, imag_part)

    def __truediv__(self, no):
        conjugate = Complex(no.real, -no.imaginary)
        denominator = no.real**2 + no.imaginary**2
        result = self * conjugate
        result.real /= denominator
        result.imaginary /= denominator
        return result

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

#19
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    # Perform integer division
    print(a // b)

    # Calculate the remainder using the modulo operator
    print(a % b)

    # Print the divmod result
    print(divmod(a, b))
#20
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())

    # Calculate and print a^b
    result_ab = pow(a, b)
    print(result_ab)

    # Calculate and print (a^b) % m
    result_ab_mod_m = pow(a, b, m)
    print(result_ab_mod_m)
#21
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    result = pow(a, b) + pow(c, d)
    print(result)
#22
for i in range(1, int(input())):
    print((10**i // 9) * i)
#23
from collections import OrderedDict

def word_count(words):
    word_dict = OrderedDict()

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict

if __name__ == '__main__':
    n = int(input())
    words = [input().strip() for _ in range(n)]

    word_dict = word_count(words)

    distinct_word_count = len(word_dict)
    occurrences = list(word_dict.values())

    print(distinct_word_count)
    print(*occurrences)
