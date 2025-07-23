# 3. Write a program to detect double space in a string. 
def main():
    user_input = input("Enter any sentence to detect double spaces :")
    print(detect_double_spaces(user_input))

def detect_double_spaces(user_input : str) -> bool:
    return user_input.count("  ") >=1

main()

# Returns True if the entered sentence contains double spaces or not