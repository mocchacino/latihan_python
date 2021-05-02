def ReverseArray(aray):
    j = len(aray)
    new_aray=[]
    for i in range(j-1, -1, -1):
        new_aray.append(aray[i])
    print(new_aray)
    
ReverseArray([105, 104, 103, 102, 101])