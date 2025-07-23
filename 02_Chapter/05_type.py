# type() function to find type of variable
# Type casting 

value_1 = 32
value_2 = "linkedIn"
res1 = type(value_1) # <class 'int'>
res2 = type(value_2) # <class 'str'> 
print(res1)
print(res2)

# instance() is used to check if a variable is of a specific type or not -> return boolean
print(isinstance(value_1,str))
print(isinstance(value_2,str))

a_value = int(input('Enter first value : '))
b_value = int(input('Enter second value : '))
print(f'The sum is {a_value + b_value}') 
''' if done without int type casting performs string concatenation as entered 
value get converted to string by default through input() function'''

