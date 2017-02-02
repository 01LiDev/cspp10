def replace(original,to_replace,replace_with):
    for x in range(len(original)):
        if original[x] == to_replace:
            original[x] = replace_with
            
original = [1,2,1,3,5,1]    
replace(original,1,"d")
print (original)