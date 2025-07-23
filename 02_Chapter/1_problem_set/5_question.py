# write a python program to find the average of given two number entered by user

def main():
    find_avg()

def find_avg() -> None:
    num1 = int(input('Enter first value :'))
    num2 = int(input('Enter second value :'))
    avg = (num1+num2)/2
    print(f'The average of {num1} and {num2} is {avg}')

main()