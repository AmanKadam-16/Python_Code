# 4. Replace the double space from problem 3 with single spaces. 
def main():
    user_input = input("Enter any sentence to detect double spaces :")
    print(replace_double_spaces(user_input))

def replace_double_spaces(user_input : str) -> bool:
    return user_input.replace("  ","   ") # replace double spaces with tripple spaces

main()
