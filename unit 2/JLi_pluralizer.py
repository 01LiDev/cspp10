num=int(input("How many:"))
word=input("Enter a word:")
new_word=word
if new_word[-2:] == "fe" and num > 1:
    print (str(num)+" "+ new_word + "ves")
elif new_word[-1:] == "y" and num > 1:
    print (str(num)+" "+ new_word + "ies")
elif new_word[-2:] == "sh" or new_word[-2:] == "ch" and num > 1:
    print (str(num)+" "+ new_word + "es")
elif new_word[-2:] == "us" and num > 1:
    print (str(num)+" "+ new_word + "i")
elif new_word[-2:] == "ay"or new_word[-2:] == "oy" or  new_word[-2:] == "ey" or  new_word[-2:] == "uy" and num > 1:
    print (str(num)+" "+ new_word + "s")
else:
    print (str(num) + " "+ new_word + "s")
    
    
    
    
    