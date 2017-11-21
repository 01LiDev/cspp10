def convdtob(n):
  
  if n>1:
    convdtob(n//2)
  print(n % 2,end = '')
dec=int(input("enter a number: "))
convdtob(dec)
  	