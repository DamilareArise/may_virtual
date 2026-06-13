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
# print(bin(val1))
# print(bin(val2))
# 10100
#  1010

# print(bin(val1 | val2)) # 11110
# print(val1 ^ val2)


# Assignment
# 1. Conditional statement 
# 2. Build a grading system.


# conditional statement (if/else statement)
x = 5
# if x > 3:
#     print("Yes")
# else:
#     print("No")
    
    
    
# food = ['rice', 'bread', 'eba']
# drinks = ['fanta', 'coke']

# request = input("Request: ")
# if request in food:
#     print(f"{request} is available")

# elif request in drinks:
#     print(f"{request} is available in drink store")

# else:
#     print(f"{request} is not available")



# 70 - 100 -> A  
# 60 - 69 -> B
# 50 - 59 -> C
# 45 - 49 -> D
# 40 - 44 -> E 
# 0 - 39 -> F

# score = int(input("Score: "))
# if score >= 70 and score <= 100:
#     print("Grade A")
# elif score >= 60 and score < 70:
#     print("Grade B")
# elif score >= 50 and score < 60:
#     print("Grade C")
# elif score >= 45 and score < 50:
#     print("Grade D")
# elif score >= 40 and score < 45:
#     print("Grade E")
# elif score >= 0 and score < 40:
#     print("Grade F")
# else:
#     print("Invalid score")


# class-work: 
# 1. build a simple calculator.
# 2. Build a simple email validator


# ussd = input("USSD: ")
# if ussd == "*312#":
#     print("""
#         1. Buy Data
#         2. Check balance
#         #. Exit
#     """)
#     choice = input("Choice: ")
#     if choice == "1":
#         print("Buy Data")
#     elif choice == "2":
#         print("Check Balance")
#     elif choice == "#":
#         exit("Goodbye!")
# else:
#     print("Invalid USSD code")


# python strings

text = "hello everyone. welcome to class." #["H", "e", "l" ....]
# print(type(text))
# print(text[3])
# print(text[-2])
# print(text[0:5])

# QA = input("What is the capital of Nigeria: ").strip()
# print(QA)
# if QA.lower() == "abuja":
#     print("Correct")
# else:
#     print("Wrong Answer")

# print(len(text.strip()))

# print(text.capitalize())
# print(text.title())
# print(text.lower())
# print(text.upper())

# print(text.strip("$%/"))
# print(text.split('.'))

# Word counter
# essay = input("Essay: ").strip()
# no_of_words = len(essay.split())
# print(f"Total words: {no_of_words}")

# item = ['hello', 'everyone.', 'welcome', 'to', 'class.']
# print("+".join(item))

# print(text.find("Everyone"))
# print(text.startswith("hello"))
# print(text.index('.', 15))

# special character
# \n - nextline
# \b - backspacee
# \r - return
# \t - tab

# escape character - \
# r - raw string 

# text = "hello everyone.\\u7685 welcome to class."
text = r"hello everyone.\u7685 welcome to class."
# print(text)


# Python Collections / Array
# 1. List [] or list() - ordered, indexed, mutable/changeable. allows duplicate item.
students = ['Zeenat', 'Blessing', 'Chris', 'Iyanu', 'Bash', 'Blessing']
# print(type(students))
# print(students[4])
# print(students[-1])
# slicing
# print(students[0:3])
# print(students[:3])
# print(students[3:])
# print(students[1][0])
# print(students[3][2])
# print(students[2][1])
# print(students[-1][-1])

# students[2] = "Christopher"

# students.append('Ayomide')
# students.insert(0, 'Ayomide')
# students.extend(["Ayomide", 'Tolulope'])

# students.pop(1)
# students.remove('Blessing')

# duplicate = students.copy()
# duplicate.pop()
# print(duplicate)

# students.reverse()
# print(students)

# print(students.index("Zeenat"))

# prices = [20, 30, 10, 50]
# print(sum(prices))
# print(min(prices))
# print(max(prices))

# print(len(prices))
# print(sum(prices)/len(prices))


# python loop
# 1. For loop - it works with iterables/sequence types

# for student in students:
#     print(student, "is a python student")

# for no in range(1, 10, 2):
#     print(no)

# for x in range(1, 5):
#     print(f"\n{x} Times Table")
#     for y in range(1, 5):
#         print(f"{x} x {y} = {x*y}")


# db = []
# slot = 10
# for x in range(slot):
#     name = input(f"Name {x + 1}: ")
#     db.append(name)
    
#     user = input("Press 1 to stop or enter to continue: ")
#     if user == "1":
#         break
    
# print(db)

# 2. While loop: Is a loop based on a condition.
# x = 5
# while x >= 0: 
#     print(x)
#     x -= 1


# x = 0
# while x <= 10:
#     print(x)
#     x += 1
# else:
#     print("Looping is done!")

# ticket = 10
# while ticket > 0: 
#     age = int(input("Age: "))
#     if age < 18:
#         print('Too young')
#         continue
    
#     if ticket == 3:
#         print("Operation terminated.")
#         break
    
#     ticket -= 1
#     print('Ticket issued. remaining', ticket)
    
        
# cart = []

# while True:
#     print("""
#         1. add to cart 
#         2. remove item
#         3. view
#         #. exit  
#     """)
#     choice = input("Choice: ").strip()
#     if choice == "1":
#         item = input("Item: ")
#         cart.append(item)
    
#     elif choice == "#":
#         exit("Goodbye!")
#         # break  
        
#     elif choice == "3":
#         print(cart)      


# print("Yooooo!!!!!") 
 
# Assignment 
# 1. Build a todo app with functionalities as; add, remove, edit, clear all, view all.


# 2. Tuple - ordered, indexed, allows duplicate, immutable/unchangeable

cars = ('Benz', 'Toyota', 'BMW', 'Audi', 'Audi')
# print(cars[0:3])
# cars = list(cars)
# cars[3] = "Bentley"

# unpacking 
# c1, *all, c2 = cars
# *c, = cars
# print(c)

# print(cars.count("BMWs"))
# print(cars.index('Toyota'))

# store = [
#     ('shirt', 1000),
#     ('Trouser', 3000),
#     ('Shoe', 5000)
# ]

# print(store)
# for item in store:
#     print(item[1])

# for item, price in store:
#     print(price)
    

# score = 0

# ques1 = input("What is the capital of Nigeria a.) Abuja b.) Lagos: ").strip()
# if ques1.lower() == "a":
#     score += 1
    
# ques2 = input("What is the capital of Nigeria a.) Abuja b.) Lagos: ").strip()
# if ques2.lower() == "a":
#     score += 1
    
# ques3 = input("What is the capital of Nigeria a.) Abuja b.) Lagos: ").strip()
# if ques3.lower() == "a":
#     score += 1


# print("Result is:", score)


score = 0

QA = [
    ("What is the capital of Nigeria a.) Abuja b.) Lagos", 'a', 10),
    ("What is the capital of Lagos a.) Abuja b.) Ikeja", 'b', 10),
    ("What is the capital of Osun a.) Osogbo b.) Lagos", 'a', 10),
    ("What is the capital of Oyo a.) Oyo b.) Osogbo", 'a', 10),
    ("What is the capital of Ondo a.) Benin b.) Akure", 'b', 10),
]

for ques, ans, mark in QA:
    print(ques)
    user_ans = input("Ans: ").strip()
    if user_ans.lower() == ans:
        score += mark
        print("Correct")
    else:
        print("Wrong")
        

print(f"Your total score is: {score}")



# 3. Set
# 4. Dictionary 
