def remove_all(original,target):
    for x in range(original.count(target)):
        original.remove(target)
            
original = [1,4,5,1,5,1]
remove_all(original,1)            
print (original)