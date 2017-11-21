import random
h = int(input("How high: "))
user = int(input("Guess the number: "))
correct=random.randint(1,h)
guesses= 0
while user != correct:
    guesses = guesses + 1
    print (user)
    if user < correct:
        print("Too low")
        user = int(input("Guess the number: "))
    elif user > correct:
        print("Too high")
        user = int(input("Guess the number: "))
    else:  
        print (user)
print ("You are correct. It took you {} tries.".format(guesses))
    
        
    
    
