String = input(" enter your string : ")
for i in String:
    count = 0
    for j in String:
        if i == j:
            count+=1
        if count > 1:
            break
    if count == 1:
        print(i,end = " ")