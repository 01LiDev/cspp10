from pprint import pprint
dict_assg = {
    'hay':'bay'
}
#This should allow the user to add a new key-value pair to the dictionary.
#Ask the user for both the key and the value.  Treat both as Strings.\
def add(dict_assg):
    key_input = input("Enter a key: ")
    return key_input
    value_input = input("Enter a value")
    return value_input
    print("New key-value pair {},{}".format(key_input,value_input))
    dict_assg[key_input] = value_input
    
#This should allow the user to remove a key-value pair from the dictionary.
#Ask the user for just the key and delete based on the key.
# def remove_key():

#This should allow the user to remove multiple key-value pairs from the 
#dictionary based on a value.  Ask the user for just a value and remove all keys 
#from the dictionary that have that value.
# def remove_value(extension):

#This should allow the user to change a key/value pair in the dictionary.
# def update():

#This should prettyprint (pprint) the dictionary.
# def p_print():

#This should run the print function and then end the program.
# def exit():

add(dict_assg)
pprint(dict_assg)



