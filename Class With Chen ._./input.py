# final=""
# inp = input("enter a number or exit:")
# while (inp != "exit"):
#     final = final+inp+" "
#     inp = input("enter a number or exit:")
    
    
# print(final)

from getpass import getpass

asdf = input("This is not secure: ")
pw = getpass("This is secure: ")

print("You typed: " + pw)