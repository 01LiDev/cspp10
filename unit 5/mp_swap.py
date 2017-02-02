def swap(values,index1,index2):
    for x in range(len(values)):
        temp = index1
        values[index1] = values[index2]
        values[index2] = values[temp]
            
values = [1,2,3,4,5,6]
swap(values,2,5)
print(values)
