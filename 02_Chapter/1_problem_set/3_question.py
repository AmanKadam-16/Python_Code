# check the type of variable assigned using type() function

def main():
    findType()
    
def findType() -> None:
    user_input = input('Enter any value :')
    data_type = type(user_input)
    print(f'The Data type of your entered value {user_input} is {data_type}')

main()