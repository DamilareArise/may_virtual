# Two categories of error
# 1. Compile type error 
# 2. runtime error  

# print(name)

# nums = range(10)
# print(nums[13])


# try and except 

# try:
#     nums = range(10)
#     print(nums[13])
    
# except IndexError as i:
#     print(f"An error occured: {i}")

# except NameError as n:
#     print(f"An error occured: {n}")

# except Exception as e:
#     print(f"An error occured: {e}")
    
    
    
try:    
    amount = float(input('Amount: ')) 
except Exception as e:
    print(f"An error occured: {e}")
else:
    # shows if there's no error
    print('Transaction successful')
    
finally:
    # shows whether there's an error or not 
    print('Repeat action or go to home')
    
    
print('Helloo....')
