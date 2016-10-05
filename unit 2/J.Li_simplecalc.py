s = input()
n1= s[1]
n2= s[4]
sign=s[2]
if sign=="+":
    s = s[1] + s[4]
if sign=="-":
    s=s[1] - s[4]
elif sign== "/":
    s = s[1]/s[4]
elif sign=="*":
    s =s[1]*s[4]
elif sign == "%":
    s =s[1]%s[4]
print ("The result is " + s)