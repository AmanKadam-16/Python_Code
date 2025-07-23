# Write a python program to display a user entered name followed by Good 
# Afternoon using input () function.

def main():
    greet()
    
def greet() -> None:
    userName = input('Hey, What\'s your name ? ')
    print(f"Good Afternoon, {userName.capitalize()}")
    
main()