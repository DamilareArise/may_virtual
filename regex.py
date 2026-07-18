import re


def validate_email(email):
    # pattern = r"^\w+@\w+\.\w+$" 
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" 
    match = re.match(pattern, email)
    if match:
        print(match)
        # print('Email is valid')
        return True
    else:
        return False
 
 
# email = input("email: ")
# if not validate_email(email):
#     print('Email is not valid')


string = "give me 200 apples and 500 pieces of tomatoes"
pattern = r"\d+"
# res = re.findall(pattern, string)
# res = re.sub(pattern, 'some', string)
# res = re.search(pattern, string)
# print(res.group())



# import math, cmath, statistics


# Bank application using python and mysql for database for management
# registration, login, withdraw, deposit, transfer, transaction history

