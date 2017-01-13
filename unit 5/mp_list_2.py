#With Jahseem
list_1 = [] 
while True:
    user = input("Enter a number, sum , clear , length , exit: ").lower()
    if user == "clear":
        list_1 = []
        print (list_1)
    elif user == "sum":
        print (sum(list_1))
    elif user == "length":
        print (len(list_1))
    elif user == "exit":
        break
    elif user == "":
        
    else:
        list_1.append(int(user))
        print (list_1)