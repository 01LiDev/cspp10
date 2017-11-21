from pprint import pprint
dict_assg = {

}
#This should allow the user to add a new key-value pair to the dictionary.
#Ask the user for both the key and the value.  Treat both as Strings.\
def add(dict_assg):
    key_input = input("Enter the word: ")
    value_input = input("Enter the definition: ")
    print("New key-value pair {},{}".format(key_input,value_input))
    if key_input not in dict_assg:
        dict_assg[key_input] = value_input
    else:
        print("Key already made")
        key_input
        value_input
#This should allow the user to remove a key-value pair from the dictionary.
#Ask the user for just the key and delete based on the key.
def remove_key(dict_assg):
    keyval_rem = input("The key you want to remove: ")
    if keyval_rem in dict_assg:
        del dict_assg[keyval_rem]

#This should allow the user to change a key/value pair in the dictionary.
def update(dict_assg):
    print("Key to be updated")
    update_user = input("Enter: ")
    if update_user in dict_assg:
        print("New Value")
        upd_val = input("Enter:")
        dict_assg[update_user] = upd_val

#This should prettyprint (pprint) the dictionary.
def p_print(dict_assg):
    pprint(dict_assg)
#This should run the print function and then end the program.
def exit():
    p_print(dict_assg)

#The main function
def main():
    print("Press Enter to continue or Exit to stop")
    options = input("Enter: ").lower()
    while options != "exit":
        print("Your options are Add|Remove|Update|Pprint|Exit")
        options = input("Enter: ").lower()
        if options == "add":
            add(dict_assg)
        elif options == "remove":
            remove_key(dict_assg)
        elif options == "update":
            update(dict_assg)
        elif options == "pprint":
            p_print(dict_assg)
        elif options == "exit":
            exit()
            break
        
        
main() 
#NotDepressed
#FGreat
#ItWorks
#BreakIt_ScrewYou


