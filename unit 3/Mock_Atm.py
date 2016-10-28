bank_account = 10000
print("1. Withdraw \n2. Deposit \n3. Exit")
choice = input("Welcome to ATM! Pick from above [1|2|3]:")
while bank_account > 0: #student completes while loop
    if choice == "1": #user chooses 'withdraw'
        withdraw =  int(input("How much to withdraw: "))
        bank_account = bank_account - withdraw
        total=bank_account
        print (total)
        break
    elif choice == "2":
        amount = int(input("How much to deposit: "))
        bank_account = bank_account + amount
        total = bank_account
        print (total)
        break
    elif choice == "3":
        print("1. Withdraw \n2. Deposit \n3. Exit")
        choice = input("Pick from above [1|2|3]:")
