list1 = []
user = 1
while user != 0:
    user = int(input("Enter a Number to list or remove:  "))
    list1.append(user)
    print ("some list :{}".format(list1))
    if user < -(user):
        user = user * -(user)
        list1.remove(user)
        print ("some list :{}".format(list1))