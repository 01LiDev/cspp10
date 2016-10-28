s = input()
n1= s[0]
n2= s[2]
sign=s[1]
total = s
if sign=="+":
    total = int(n1) + int(n2)
    print ("The result is " + str(total))
if sign=="-":
    total= int(n1) - int(n2)
    print ("The result is " + str(total))
elif sign== "/":
    total = int(n1)/int(n2)
    print ("The result is " + str(total))
elif sign=="*":
    total = int(n1)*int(n2)
    print ("The result is " + str(total))
elif sign == "%":
    total = int(n1)%int(n2)
    print ("The result is " + str(total))
else: 
    print ("none")


