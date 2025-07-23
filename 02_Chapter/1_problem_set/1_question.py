# write a simple python program to add two numbers
def main():
    add()

def add() -> None:
    num1 : int = int(input('Enter first number :'))
    num2 : int = int(input('Enter second number :'))
    print(f'The sum of {num1} and {num2} is {num1+num2}')

main()
        