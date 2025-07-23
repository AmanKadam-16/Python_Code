# 2. Write a program to fill in a letter template given below with name and date. 
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''

def main():
    userName = input("Enter candidate name : ")
    date = input("Enter Date : ")
    msg = frame_message(userName, date, letter)
    print(msg)
    
def frame_message(name: str, date: str, template : str) -> str:
    msg_template = template.replace("<|Name|>", name).replace("<|Date|>", date)
    return msg_template

main()