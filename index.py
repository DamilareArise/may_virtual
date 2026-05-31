# print("Hello world")
# print(""" 
#     mskas kfnkass lnsanas
#     ,,as.a snsnsksn
#     msna,sn 
# """)

# Python output command
# commenting
# Identation

# print("Hello Zeenat")


# Python variables

name = "Demilade"
bottle = "water"
# print(bottle)

name = "Zeenat"

# print(name)

# rules of guiding variable declaration 

# 1. A variable can only start with underscore any an alphabet
# 2. A variable name can only contain alphabets, number and underscore
# 3. A variable name doesnt include spaces
# i. camel casing - firstNameOfTheStudent
# ii. Pascal casing - FirstNameOfTheStudent
# iii. Snake casing - first_name_of_the_student
# 4. Your variable must be descriptive enough


# types of variable declaration 

# 1. single variable single value 
name = "Ayomide"
# 2. single variable multiple values
students = "Ayomide", "Olamide", "John"
# print(students)
# 3.  multiple variable single value 
x = y = z = 10
x = 20
# print(x)
# 4. multiple variable mutiple Value
a, b, c = 10, 20, 30
# print(c)

# name = input("Your name: ")
# print(type(name))
age = 30

# concatenation - ability join two or more strings type together
# print("My name is " + name + ". I am " + str(age) + "years old")
# print(f"My name is {name}. I am {age} years old")

# class-work - create atleast 5 variables that tells us about yourself, use them to create a sentence using the two concatenating approaches

# python datatypes 

# 1. Text type: strings
name = "Ayomide"
# print(type(name))

# 2. Number type:
    # i. int - 1, 12, 300
    # ii. float - 1.3, 35.2
    # iii. complex - 2 + 3j
    
# num = 10.2 + 3j
# print(type(num))

# 3. Sequence type
    # i. tuple - (1, 3, 5, 6)
    # ii. list - [1, 3, 5, 6]
    # iii. range()
     
# numbers = (1, 3, 5, 6)
# numbers = [1, 3, 5, 6]

# numbers = range(2, 12, 2)

# print(type(numbers))
# print(tuple(numbers))

# 4. Boolean type - False, True

# isEducated = True
# print(type(isEducated))

# print(int(isEducated))


# 5. Set Type - set() - {1, 3, 5, 6} 
numbers = {1, 3, 5, 6, 2, 4}
students = {"Ayomide", "Olamide", "John"}
# print(type(numbers))
# print(students)

#6. mapping type - dict()
student = {
    "name": "Ola Oba",
    "age": 20,
    "isActive": True 
}

# print(type(student))
# print(student["name"])


# 7. None type 
# number = None
# print(type(number))



# Python operators:
# 1. Arithmetic operator: +, -, /, *, **, //, %
# print(5**2)
# print(5//2)
# print(5%2)

# 2. Assignment operator: =, +=, -=, /= .. e.t.c
x = 5
# x+=5 
# x-=2
# print(x)

# 3. Comparison operator: ==, !=, >, <, >=, <=
x = 5
# print(x >= 6)

# 4. Logical operator: AND, OR, NOT
"""
A ---- B ---- AND ---- OR ---- XOR
0      0       0        0       0
0      1       0        1       1
1      0       0        1       1
1      1       1        1       0

NOT A
1
1
0
0

"""

age = 2
paymentStatus = True
# print(age >= 18 or paymentStatus)
# print(not paymentStatus)

# 5. Identity Operator: is, is not
# print(age is not x)

# 6. membership operator: in, not in
students = ["Lola", "ade", "shola"]
# print("lola" not in students)

# 7. bitwise operator: 
# & -> AND 
# | -> OR 
# ~ -> NOT
# ^ -> XOR
val1 = 20
val2 = 10
print(bin(val1))
print(bin(val2))
# 10100
#  1010

# print(bin(val1 | val2)) # 11110
# print(val1 ^ val2)


# Assignment
# 1. Conditional statement 
# 2. Build a grading system.