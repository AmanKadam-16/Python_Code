# write a python program to find the square of number entered by user

def main():
    user_input = int(input('Enter any number of which you want to find a square of :'))
    print(find_sqr(user_input))

def find_sqr(val : int) -> int:
    sqr = val**2
    return sqr

main()