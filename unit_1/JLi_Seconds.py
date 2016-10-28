#seconds= remander of the seconds input -_-
#minute=60 seconds
#hour=3600 seconds
s= int(input())
m=s/60 
seconds=s%60
hour= m/60
hour=s/3600
print( str(int(hour)) + " hour " + str(int(m)) + " minute " + str(int(seconds)) + " seconds ")

